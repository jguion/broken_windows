from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from boston_disorder.models import *
import boston_disorder.utils as utils
from django.db.models import Min, Max, Count
from collections import defaultdict
import simplejson as json
from geopy import geocoders
import time
import datetime
import math
from django.db.models import Q

DISTRICT_NAMES = {
	'1': 'Allston/Brighton',
	'2': 'Back Bay',
	'3': 'Bay Village',
	'4': 'Beacon Hill',
	'5': 'Charlestown',
	'6': 'Chinatown/Leather District',
	'7': 'Dorchester',
	'8': 'Downtown/Financial District',
	'9': 'East Boston',
	'10': 'Fenway/Kenmore',
	'11': 'Hyde Park',
	'12': 'Jamaica Plain',
	'13': 'Mattapan',
	'14': 'Mission Hill',
	'15': 'North End',
	'16': 'Roslindale',
	'17': 'Roxbury',
	'18': 'South Boston',
	'19': 'South End',
	'20': 'West End',
	'21': 'West Roxbury'
	}

HOUSING_ISSUES_CODES = [
	"Bed Bugs", #12, #Bed Bugs
	"Breathe Easy",#18, #Breathe Easy
	"Chrnoic Dampness / Mold",#26, #Chrnoic Dampness / Mold
	"Heat - Excessive, Insufficient",#50, #Heat - Excessive, Insufficient
	"Maintenance Complaint - Residential",#68, #Maintenance Complaint - Residential
	"Mice Infestation - Residential",#71, #Mice Infestation - Residential
	"Pest Infestation - Residential",#107, #Pest Infestation - Residential
	"Poor Ventilation",#113, #Poor Ventilation
	"Squalid Living Conditions",#147, #Squalid Living Conditions
	"Unsatisfactory Living Conditions",#165, #Unsatisfactory Living Conditions
	"Unsatisfactory Utilities - Electrical, Plumbing",#166, #Unsatisfactory Utilities - Electrical, Plumbing
]

UNCIVIL_USE_OF_SPACE_CODES = [
	"Abandoned Building",#3, #Abandoned Building
	"Illegal Occupancy",#55, #Illegal Occupancy
	"Illegal Rooming House",#57, #Illegal Rooming House
	"Maintenance - Homeowner",#67, #Maintenance - Homeowner
	"Parking on Front/Back Yards (Illegal Parking)",#103, #Parking on Front/Back Yards (Illegal Parking)
	"Poor Conditions of Property",#112, #Poor Conditions of Property
	"Trash on Vacant Lot",#157, #Trash on Vacant Lot
]

BIG_BUILDINGS_CODES = [
	"Big Buildings Enforcement",#13, #Big Buildings Enforcement
	"Big Buildings Online Request",#14, #Big Buildings Online Request
	"Big Buildings Resident Complaint",#15, #Big Buildings Resident Complaint
]

GRAFFITI_CODES = [
	"Graffiti Removal",#49, #Graffiti Removal
	"PWD Graffiti",#96, #PWD Graffiti
]

TRASH_CODES = [
	"Abandoned Bicycle",#2, #Abandoned Bicycle
	"Empty Litter Basket",#37, #Empty Litter Basket
	"Illegal Dumping",#54, #Illegal Dumping
	"Improper Storage of Trash (Barrels)",#60, #Improper Storage of Trash (Barrels)
	"Rodent Activity",#131, #Rodent Activity
]

NO_FACTOR_CODES = [
	"Illegal Auto Body Shop",#53, #Illegal Auto Body Shop
	"Illegal Posting of Signs",#56, #Illegal Posting of Signs
	"Illegal Use",#58, #Illegal Use
	"Overflowing or Un-kept Dumpster",#95, #Overflowing or Un-kept Dumpster
	"Pigeon Infestation",#110, #Pigeon Infestation
]

PRIVATE_CODES = HOUSING_ISSUES_CODES + BIG_BUILDINGS_CODES + UNCIVIL_USE_OF_SPACE_CODES
PUBLIC_CODES = GRAFFITI_CODES + TRASH_CODES
PHYSICAL_DISORDER_CODES = PRIVATE_CODES + PUBLIC_CODES

PUBLIC_SOCIAL_DISORDER = {"socdis":True}
SOCIAL_STRIFE = {"socstrife":True}
ALCOHOL = {"alcohol":True}
INTERPERSONAL_VIOLENCE = {"violence":True}
GUNS = {"guns":True}
MAJOR_MEDICAL_EMERGENCIES = {"majormed":True}
RESPIRATORY_AND_OBGYN = {"youthhealth":True}
NO_MED = {"majormed":True, "no_med":False}

SOCIAL_DISORDER = Q(**PUBLIC_SOCIAL_DISORDER) | Q(**SOCIAL_STRIFE) | Q(**ALCOHOL)
VIOLENCE = Q(**INTERPERSONAL_VIOLENCE) | Q(**GUNS)
MEDICAL_EMERGENCIES = Q(**MAJOR_MEDICAL_EMERGENCIES) | Q(**RESPIRATORY_AND_OBGYN) | Q(**NO_MED)
ALL_911_CALLS = Q(SOCIAL_DISORDER) | Q(VIOLENCE) | Q(MEDICAL_EMERGENCIES)

FILTER_DICT = {
	"physical_disorder":PHYSICAL_DISORDER_CODES,
	"public":PUBLIC_CODES,
	"private":PRIVATE_CODES,
	"housing":HOUSING_ISSUES_CODES,
	"uncivil_use":UNCIVIL_USE_OF_SPACE_CODES,
	"big_buildings":BIG_BUILDINGS_CODES,
	"graffiti":GRAFFITI_CODES,
	"trash":TRASH_CODES,
	"social_disorder":SOCIAL_DISORDER,
	"all_911_calls":ALL_911_CALLS,
	"public_social_disorder":PUBLIC_SOCIAL_DISORDER,
	"socstrife":SOCIAL_STRIFE,
	"alcohol":ALCOHOL,
	"violence":VIOLENCE,
	"interpersonal_violence":INTERPERSONAL_VIOLENCE,
	"guns":GUNS,
	"medical_emergency":MEDICAL_EMERGENCIES,
	"major_medical_emergency":MAJOR_MEDICAL_EMERGENCIES,
	"youth_health":RESPIRATORY_AND_OBGYN,
	"no_med":NO_MED
}

TYPE_DISPLAY_NAMES = {
	"physical_disorder":"Physical Disorder",
	"public":"Public Denigration",
	"private":"Private Neglect",
	"housing":"Housing Issues",
	"uncivil_use":"Uncivil Use of Space",
	"big_buildings":"Big Building Complaints",
	"graffiti":"Graffiti",
	"trash":"Trash",
	"all_911_calls":"911 Calls",
	"social_disorder":"Social Disorder",
	"socstrife":"Social Strife",
	"alcohol":"Alcohol",
	"violence":"Violence",
	"guns":"Guns",
	"medical_emergency":"Medical Emergencies",
	"youth_health":"Youth Health",
	"major_medical_emergency":"Major Medical",
	"no_med":"No Med"
}


def crm(request, l1=None):
	dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
	filter_args = {}#dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	for key, item in request.GET.items():
		if key.startswith('f_'):
			if key.endswith("__in") and item.startswith("list("):
				item = [x.strip() for x in item[5:-1].split(",")]
			filter_args[key[2:]] = item

	show_details = request.GET.get('show_details', False)
	if request.GET.get('granularity'):
		granularity = request.GET.get('granularity')
		is_default = False
	else:
		granularity = "Block Group"
		is_default = True

	map_type = request.GET.get('map_type', "heat_map")

	remove_block_group = lambda x:x[:12]+x[13:]

	area_identifier = None
	if granularity == "Census Tract":
		area_identifier ='ct_id'
	elif granularity == "Block Group":
		area_identifier = 'bg_id'
	elif granularity == "Block":
		area_identifier = 'blk_id'


	address_to_coordinates = None

	blocks_to_coordinates = (dict((x['areaid'], x) for x in
									TigerData.objects.filter(type=granularity)
									.values("areaid", "latitude", "longitude")))

	def get_areaid(x):
		if granularity == "Census Tract":
			return str(x['ct_id'])
		elif granularity == "Block Group":
			return str(x['bg_id'])
		elif granularity == "Block":
			return remove_block_group(str(x['blk_id']))
		else:
			return None

	def get_coordinates(x):
		areaid = get_areaid(x)
		return blocks_to_coordinates.get(areaid) if areaid else None

	
	bg_population = (dict((x['bg_id'], (x['totalpop'], x['popden'], x['area'])) for x in (BostonBlockGroup.objects
													.values("totalpop", "bg_id", "popden", "area"))))
	crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
	data = {}
	if l1:
		crm_filter = FILTER_DICT.get(l1)
		display_type = TYPE_DISPLAY_NAMES.get(l1)
		crm = (crm.filter(type__in=crm_filter).values('location', 'city', 'state', 'open_dt', 
					'reason', 'subject', 'type', 'nsa_name', 'bg_id', 'blk_id', 'ct_id'))
		areas = []
		mean = None
		std_dev = None
		lower_interquartile_range = None
		median = None
		upper_interquartile_range = None
		if granularity != "Address":
			areas = ([{"areaid":info[area_identifier],"nsa_name":info['nsa_name'], "count":info['pk__count'],
					   "coordinates":get_coordinates(info), "pop":bg_population.get(info['bg_id'])[0], 
					   	"popden":bg_population.get(info['bg_id'])[1], "area":bg_population.get(info['bg_id'])[2]} for info in 
								crm.values(area_identifier).distinct().annotate(Count('pk'))
									.values("nsa_name","pk__count",area_identifier, 'bg_id').order_by('-pk__count')
									 if info[area_identifier] is not None]
					if area_identifier else [])

			counts = list(x['count'] for x in areas)
			mean = sum(counts, 0.0) / len(counts) if counts else 0
			d = [ (i - mean) ** 2 for i in counts]
			std_dev = math.sqrt(sum(d) / len(d)) if d else 0
			
			z = len(counts)
			if z >=4:
				lower_interquartile_range = counts[z/4]
				median = counts[z/2]
				v = counts[(z * 3)/4]

		locations = []
		for i, entry in enumerate(crm):
			res = {}
			areaid = get_areaid(entry)		
			address = "%s, %s, %s"%(entry['location'], entry['city'], entry['state'])
			address_coordinate = None
			if is_default or not areaid:
				if address_to_coordinates is None:
					address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
				address_coordinates = address_to_coordinates.get(address)
				res['address_latitude'] = float(address_coordinates['latitude']) if address_coordinates else None
				res['address_longitude'] = float(address_coordinates['longitude']) if address_coordinates else None
	
			if areaid: 
				coordinates = blocks_to_coordinates.get(areaid)
			else:
				areaid = address
				coordinates = address_coordinates

			if coordinates:
				res['latitude'] = float(coordinates['latitude'])
				res['longitude'] = float(coordinates['longitude'])
			else:
				continue
				res = utils.get_lat_long(address)
				if not res:
					continue
				item = AddressLatLog(address=address, latitude=res['latitude'],
				 				longitude=res['longitude'])
				item.save()
				time.sleep(.2)

			res['date'] = entry['open_dt']
			res['bg_id'] = str(entry['bg_id'])
			res['areaid'] = str(areaid)
			res['address'] = address
			res['subject'] = "%s, %s"%(entry['subject'],entry['reason'])
			res['type'] = "%s"%entry['type']
			locations.append(res)
		locations = sorted(locations, key=lambda x: (x['address'], x['date']))

		data = json.dumps({'locations':locations,'area_info':areas, #'areas':neighborhoods,
						   'show_details':show_details, 'granularity':granularity, 
						   'area_identifier':area_identifier, 'mean':mean, 'std_dev':std_dev,
						   'map_type':map_type, 'lower_interquartile_range':lower_interquartile_range,
						   'upper_interquartile_range':upper_interquartile_range, 'median':median,
						   'is_default':is_default},
						    default=dthandler)

		return render_to_response('map.html',
								 {'data':data, 'type':l1, 'granularity':granularity, 'map_type':map_type,
								  'display_type':display_type, 'data_type':'Physical'},
								  context_instance=RequestContext(request))
	return render_to_response('map.html',{'data':data}, context_instance=RequestContext(request))

def calls(request, l1=None):
	dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
	filter_args = dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	for key, item in request.GET.items():
		if key.startswith('f_'):
			if key.endswith("__in") and item.startswith("list("):
				item = [x.strip() for x in item[5:-1].split(",")]
			filter_args[key[2:]] = item
	show_details = request.GET.get('show_details', False)
	if request.GET.get('granularity'):
		granularity = request.GET.get('granularity')
		is_default = False
	else:
		granularity = "Block Group"
		is_default = True
	map_type = request.GET.get('map_type', "heat_map")

	remove_block_group = lambda x:x[:12]+x[13:]

	area_identifier = None
	if granularity == "Census Tract":
		area_identifier ='ct_id'
	elif granularity == "Block Group":
		area_identifier = 'bg_id'
	elif granularity == "Block":
		area_identifier = 'blk_id'


	address_to_coordinates = None
	#address_to_coordinates = (dict((x['address'], x) for x in 
	#								AddressLatLog.objects.values("address", "latitude", "longitude")))
	blocks_to_coordinates = (dict((x['areaid'], x) for x in
									TigerData.objects.filter(type=granularity)
									.values("areaid", "latitude", "longitude")))

	def get_areaid(x):
		if granularity == "Census Tract":
			return str(x['ct_id'])
		elif granularity == "Block Group":
			return str(x['bg_id'])
		elif granularity == "Block":
			return remove_block_group(str(x['blk_id']))
		else:
			return None

	def get_coordinates(x):
		areaid = get_areaid(x)
		return blocks_to_coordinates.get(areaid) if areaid else None

	
	bg_population = (dict((x['bg_id'], (x['totalpop'], x['popden'], x['area'])) for x in (BostonBlockGroup.objects
													.values("totalpop", "bg_id", "popden", "area"))))
	calls = []
	data = {}
	if l1:
		call_type = FILTER_DICT.get(l1)
		display_type = TYPE_DISPLAY_NAMES.get(l1)

		if type(call_type) == dict:
			calls = Boston911Calls.objects.filter(**call_type)
		else:
			calls = Boston911Calls.objects.filter(call_type)

		if filter_args: 
			calls = calls.filter(**filter_args)

		areas = []
		mean = None
		std_dev = None
		lower_interquartile_range = None
		median = None
		upper_interquartile_range = None
		if granularity != "Address":
			areas = ([{"areaid":info[area_identifier],"nsa_name":info['nsa_name'], "count":info['pk__count'],
					   "coordinates":get_coordinates(info), "pop":bg_population.get(info['bg_id'])[0], 
					   	"popden":bg_population.get(info['bg_id'])[1], "area":bg_population.get(info['bg_id'])[2]} for info in 
								calls.values(area_identifier).distinct().annotate(Count('pk'))
									.values("nsa_name","pk__count",area_identifier, 'bg_id').order_by('-pk__count')
									 if info[area_identifier] is not None]
					if area_identifier else [])

			counts = [x['count'] for x in areas]
			if counts:
				mean = sum(counts, 0.0) / len(counts)
				d = [ (i - mean) ** 2 for i in counts]
				std_dev = math.sqrt(sum(d) / len(d))

				z = len(counts)
				lower_interquartile_range = counts[z/4]
				median = counts[z/2]
				v = counts[(z * 3)/4]

		locations = []
		for i, entry in enumerate(calls.values()):
			res = {}
			address = "%s"%(entry['match_text'])
			areaid = get_areaid(entry)

			if is_default:
				if address_to_coordinates is None:
					address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
				address_coordinates = address_to_coordinates.get(address)
				res['address_latitude'] = float(address_coordinates['latitude']) if address_coordinates else None
				res['address_longitude'] = float(address_coordinates['longitude']) if address_coordinates else None

			if areaid: 
				coordinates = blocks_to_coordinates.get(areaid)
			else:
				areaid = address
				coordinates = address_coordinates
			
			if coordinates:
				res['latitude'] = float(coordinates['latitude'])
				res['longitude'] = float(coordinates['longitude'])
			else:
				continue
				res = utils.get_lat_long(address)
				if not res:
					continue
				item = AddressLatLog(address=address, latitude=res['latitude'],
				 				longitude=res['longitude'])
				item.save()
				time.sleep(0.5)

			res['date'] = entry['close_dt']
			res['bg_id'] = str(entry['bg_id'])
			res['areaid'] = str(areaid)
			res['address'] = address
			res['subject'] = "Subject"
			res['type'] = "%s"%entry['type_desc']
			locations.append(res)
		locations = sorted(locations, key=lambda x: (x['address'], x['date']))

		data = json.dumps({'locations':locations,'area_info':areas, #'areas':neighborhoods,
						   'show_details':show_details, 'granularity':granularity, 
						   'area_identifier':area_identifier, 'mean':mean, 'std_dev':std_dev,
						   'map_type':map_type, 'lower_interquartile_range':lower_interquartile_range,
						   'upper_interquartile_range':upper_interquartile_range, 'median':median,
						   'is_default':is_default},
						    default=dthandler)

		return render_to_response('map.html',
						{'data':data,'type':l1, 'granularity':granularity, 'map_type':map_type,
						 'display_type':display_type, 'data_type':'Social'},
						 context_instance=RequestContext(request))
	return render_to_response('map.html',{'data':data}, context_instance=RequestContext(request))

def more_info(request):
	return render_to_response('more_info.html',{}, context_instance=RequestContext(request))

