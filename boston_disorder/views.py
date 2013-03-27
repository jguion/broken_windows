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

FILTER_DICT = {
	"physical_disorder":PHYSICAL_DISORDER_CODES,
	"public":PUBLIC_CODES,
	"private":PRIVATE_CODES,
	"housing":HOUSING_ISSUES_CODES,
	"uncivil_use":UNCIVIL_USE_OF_SPACE_CODES,
	"big_buildings":BIG_BUILDINGS_CODES,
	"graffiti":GRAFFITI_CODES,
	"trash":TRASH_CODES
}

def crm(request, l1=None, l2=None, l3=None, l4=None):
	dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
	filter_args = dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	show_details = request.GET.get('show_details', False)
	granularity = request.GET.get('granularity', "Block Group")
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

	
	bgs = (dict((x['bg_id'], x['totalpop']) for x in BostonBlockGroup.objects.values("totalpop", "bg_id")))
	crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
	data = {}
	if l1:
		crm_filter = FILTER_DICT.get(l1)
		crm = (crm.filter(type__in=crm_filter).values('location', 'city', 'state', 'open_dt', 
					'reason', 'subject', 'type', 'nsa_name', 'bg_id', 'blk_id', 'ct_id'))
		# neighborhoods = ([{"bg_id":info['bg_id'],"nsa_name":info['nsa_name'], "count":info['pk__count'],
		# 					"ct_id":info['ct_id'], "pop":bgs.get(info['bg_id'])} for info in 
		# 					crm.values("bg_id").distinct().annotate(Count('pk'))
		# 						.values("nsa_name","pk__count","bg_id", "ct_id")
		# 						 if info['bg_id'] is not None])
		areas = []
		mean = None
		std_dev = None
		lower_interquartile_range = None
		median = None
		upper_interquartile_range = None
		if granularity != "Address":
			areas = ([{"areaid":info[area_identifier],"nsa_name":info['nsa_name'], "count":info['pk__count'],
					   "coordinates":get_coordinates(info)} for info in 
								crm.values(area_identifier).distinct().annotate(Count('pk'))
									.values("nsa_name","pk__count",area_identifier).order_by('pk__count')
									 if info[area_identifier] is not None]
					if area_identifier else [])

			counts = [x['pk__count'] for x in 
						(BostonCRM.objects.filter(type__in=crm_filter)
						 .values(area_identifier).distinct().annotate(Count('pk'))
						 .values("pk__count").order_by('pk__count'))]
			mean = sum(counts, 0.0) / len(counts)
			d = [ (i - mean) ** 2 for i in counts]
			std_dev = math.sqrt(sum(d) / len(d))

			print "**** mean %s"%mean
			print "**** sd %s"%std_dev

			z = len(counts)
			lower_interquartile_range = counts[z/4]
			median = counts[z/2]
			v = counts[(z * 3)/4]

		# min_area = None
		# max_area = None
		# for area in areas:
		# 	if min_area is None or area["count"] < min_area:
		# 		min_area = area["count"]
		# 	if max_area is None or area["count"] > max_area:
		# 		max_area = area["count"]

		locations = []
		for i, entry in enumerate(crm):
			res = {}
			address = "%s, %s, %s"%(entry['location'], entry['city'], entry['state'])
			areaid = get_areaid(entry)
			
			if areaid: 
				coordinates = blocks_to_coordinates.get(areaid)
			else:
				areaid = address
				if address_to_coordinates is None:
					address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
				coordinates = address_to_coordinates.get(address)
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
			res['subject'] = "%s, %s"%(entry['subject'],entry['reason'])
			res['type'] = "%s"%entry['type']
			locations.append(res)

		data = json.dumps({'locations':locations,'area_info':areas, #'areas':neighborhoods,
						   'show_details':show_details, 'granularity':granularity, 
						   'area_identifier':area_identifier, 'mean':mean, 'std_dev':std_dev,
						   'map_type':map_type, 'lower_interquartile_range':lower_interquartile_range,
						   	'upper_interquartile_range':upper_interquartile_range, 'median':median},
						    default=dthandler)

		return render_to_response('map.html',{'data':data}, context_instance=RequestContext(request))
	return render_to_response('map.html',{'data':data}, context_instance=RequestContext(request))

def crm_tree(request, l1):
	data = []
	filter_args = dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
	bgs = (dict((x['bg_id'], x['totalpop']) for x in 
				BostonBlockGroup.objects.values("totalpop", "bg_id", "nbhdCRM")))
	if l1:
		crm_filter = FILTER_DICT.get(l1)
		crm = (crm.filter(type__in=crm_filter)
					.values('neighborhood', "bg_id"))
		neighborhood_counts = defaultdict(lambda : defaultdict(int))
		#neighborhood_counts = defaultdict(int)
		neighborhood_populations = defaultdict(float)
		columns = ["Location", "Parent", "Inspection Violation Count", "Color"]
		boston = ["Boston Area", '', 0, 0]
		data.append(columns)
		data.append(boston)
		for i, entry in enumerate(crm):
			neighborhood = entry['neighborhood']
			bg_id = entry['bg_id']
			if neighborhood:
				neighborhood_counts[neighborhood][bg_id] += 1
				neighborhood_populations[neighborhood] += bgs.get(bg_id, 0.0)
				#neighborhood_counts[entry['neighborhood']] += 1
		for neighborhood, count in neighborhood_counts.items():
			n_sum = sum(count.values())
			n_pop = neighborhood_populations[neighborhood]
			n_color = float(n_sum) / n_pop
			if neighborhood:
				print "%s, %s"%(neighborhood, n_color)
				data.append([str(neighborhood), "Boston Area", n_sum , n_color])

		for neighborhood, bg_info in neighborhood_counts.items():
			for bg_id, count in bg_info.items():
				population =  bgs.get(bg_id)
				color = count / population if population else 0
				if bg_id:
					print "%s, %s"%(bg_id, color)
					data.append([str("%s_%s"%(bg_id,neighborhood)), str(neighborhood), count, color])
	return render_to_response('tree_map.html',{'data':data}, context_instance=RequestContext(request))

"""
def map(request, objects):
	dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
	filter_args = dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
	if objects == "b_and_e":
		b_and_e = Crime.objects.filter(crimecode_description__contains="B&E")\
			.values("location_1", "crimecode_description", "fromdate","crimecode_description",
					"buildingtype", "placeofentry")
		locations = []
		j = len(b_and_e) - 1
		while j > 0:
			res = utils.parse_lat_lng(b_and_e[j]["location_1"])
			if res:
				date = b_and_e[j]["fromdate"]
				desc = b_and_e[j]["crimecode_description"]
				building_type = b_and_e[j]["buildingtype"]
				place_of_entry = b_and_e[j]["placeofentry"]
				res['desc'] = "%s: %s \n %s - %s"%(date,desc,place_of_entry,building_type)
				locations.append(res)
			time.sleep(.15)
			j -= 1
		data = json.dumps({'locations':locations})
		#print data
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))
	elif objects == "911_calls":
		calls = BostonCAD.objects.filter(**filter_args) if filter_args else BostonCAD.objects
		calls = (calls.values("matchxcoordinate","matchycoordinate","type_desc","priority",
					"disorder","medemerg","violent", "match_test", "close_dt"))
		locations = []
		for i, call in enumerate(calls):
			res = {}
			coordinates = address_to_coordinates.get(call['match_test'])
			if coordinates:
				res['latitude'] = coordinates['latitude']
				res['longitude'] = coordinates['longitude']
			else:
				continue
				res = utils.get_lat_long(call['match_test'])
				if not res:
					print i
					continue
				item = AddressLatLog(address=call['match_test'], latitude=res['latitude'],
				 				longitude=res['longitude'])
				item.save()
				time.sleep(.2)

			additional_info = ""
			if call['disorder']:
				additional_info += " Disorder "
			if call['medemerg']:
				additional_info += " Medical Emergency "
			if call['violent']:
				additional_info == " Violent "

			res['date'] = call['close_dt']
			res['desc'] = ("%s \n priority %s \n %s"%
				(call['type_desc'], call['priority'], additional_info))
			locations.append(res)
		data = json.dumps({'locations':locations}, default=dthandler)
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))
	elif objects == "fire":
		fires = BostonFire.objects.filter(**filter_args) if filter_args else BostonFire.objects
		fires = (fires.values("address_zip", "total_loss", "descript_b", "aim_date"))
		locations = []
		for i,fire in enumerate(fires):
			res = {}
			coordinates = address_to_coordinates.get(fire['address_zip'])
			if coordinates:
				res['latitude'] = coordinates['latitude']
				res['longitude'] = coordinates['longitude']
			else:
				continue
				res = utils.get_lat_long(fire['address_zip'])
				if not res:
					continue
				item = AddressLatLog(address=fire['address_zip'], latitude=res['latitude'],
				 				longitude=res['longitude'])
				item.save()
				time.sleep(.25)
			res['date'] = fire['aim_date']
			res['desc'] = "%s : %s"%(fire['descript_b'], fire['total_loss'])
			locations.append(res)
			#print i
		data = json.dumps({'locations':locations}, default=dthandler)
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))
	elif objects == "inspection_violations":
		inspection_violations = (BostonInspectionViolation.objects.filter(**filter_args) if filter_args 
														else BostonInspectionViolation.objects)
		inspection_violations = (inspection_violations.values("stno","stname","suffix","city","state","zip", 
						"violationdate","caseinfostatus", "descript", "comments", "paiddttm"))

		locations = []
		for i, iv in enumerate(inspection_violations):
			res = {}
			address = "%s %s %s, %s, %s 0%s"%(iv['stno'], iv['stname'], iv['suffix'],
											iv['city'], iv['state'], iv['zip'])
			coordinates = address_to_coordinates.get(address)
			if coordinates:
				res['latitude'] = coordinates['latitude']
				res['longitude'] = coordinates['longitude']
			else:
				continue
				res = utils.get_lat_long(address)
				if not res:
					continue
				item = AddressLatLog(address=address, latitude=res['latitude'],
				 				longitude=res['longitude'])
				item.save()
				time.sleep(.2)
			res['date'] = iv['violationdate']
			res['desc'] = "%s : %s"%(iv['caseinfostatus'], iv['descript'])
			locations.append(res)
			#print i
		data = json.dumps({'locations':locations}, default=dthandler)
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))
	elif objects == "crm":
		crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
		crm_filter = (HOUSING_ISSUES_CODES + UNCIVIL_USE_OF_SPACE_CODES +
					 BIG_BUILDINGS_CODES + GRAFFITI_CODES + TRASH_CODES)
		crm = (crm.filter(type__in=crm_filter)
				  .values('location', 'city', 'state', 'open_dt', 'reason', 'subject', 'type'))
		print len(crm)
		locations = []
		for i, entry in enumerate(crm):
			res = {}
			address = "%s, %s, %s"%(entry['location'], entry['city'], entry['state'])
			coordinates = address_to_coordinates.get(address)
			if coordinates:
				res['latitude'] = coordinates['latitude']
				res['longitude'] = coordinates['longitude']
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
			res['desc'] = "%s, %s, %s"%(entry['subject'],entry['reason'],entry['type'])
			locations.append(res)
			if not i % 100:
				print i
		data = json.dumps({'locations':locations}, default=dthandler)
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))

	else:
		data = json.dumps({'locations':[]})
		return render_to_response('maps1.html',{'data':data}, context_instance=RequestContext(request))

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

def tree_map(request, objects):
	data = []
	filter_args = dict((key[2:], item) for key, item in request.GET.items() if key.startswith('f_'))
	if objects == "911_calls":
		calls = BostonCAD.objects.filter(**filter_args) if filter_args else BostonCAD.objects
		calls = (calls.values("matchxcoordinate","matchycoordinate","type_desc","priority",
					"disorder","medemerg","violent", "match_test", "close_dt"))
		neighborhood_counts = defaultdict(int)
		columns = ["Location", "Parent", "911 Call Count", "Color"]
		boston = ["Boston Area", '', 0, 0]
		data.append(columns)
		data.append(boston)
		for call in calls:
			neighborhood_info = call['match_test'].split(',')
			if neighborhood_info and len(neighborhood_info) > 1:
				neighborhood = str(neighborhood_info[1].strip())
				neighborhood_counts[neighborhood] += 1
		for neighborhood, count in neighborhood_counts.items():
			data.append([neighborhood, "Boston Area", count, 0])
	elif objects == "fire":
		fires = BostonFire.objects.filter(**filter_args) if filter_args else BostonFire.objects
		fires = (fires.values("address_zip", "total_loss", "descript_b", "aim_date", "district"))
		neighborhood_counts = defaultdict(int)
		columns = ["Location", "Parent", "Fire Count", "Color"]
		boston = ["Boston Area", '', 0, 0]
		data.append(columns)
		data.append(boston)
		for fire in fires:
			if fire["district"]:
				district = (DISTRICT_NAMES[str(fire['district'])] if DISTRICT_NAMES.get(str(fire["district"]))
							else str(fire['district']))

				neighborhood_counts[district] += 1
		for neighborhood, count in neighborhood_counts.items():
			data.append([neighborhood, "Boston Area", count, 0])
	elif objects == "inspection_violations":
		inspection_violations = (BostonInspectionViolation.objects.filter(**filter_args) if filter_args 
														else BostonInspectionViolation.objects)
		inspection_violations = (inspection_violations.values("stno","stname","suffix","city","state","zip", 
						"violationdate","caseinfostatus", "descript", "comments", "paiddttm"))
		neighborhood_counts = defaultdict(int)
		columns = ["Location", "Parent", "Inspection Violation Count", "Color"]
		boston = ["Boston Area", '', 0, 0]
		data.append(columns)
		data.append(boston)
		for iv in inspection_violations:
			if iv['city']:
				neighborhood_counts[str(iv['city'])] += 1
		for neighborhood, count in neighborhood_counts.items():
			data.append([neighborhood, "Boston Area", count, 0])
	elif objects == "crm":
		crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
		crm_filter = (HOUSING_ISSUES_CODES + UNCIVIL_USE_OF_SPACE_CODES +
					 BIG_BUILDINGS_CODES + GRAFFITI_CODES + TRASH_CODES)
		crm = (crm.filter(code__in=crm_filter)
					.values('city','neighborhood'))
		#neighborhood_counts = defaultdict(lambda : defaultdict(int))
		neighborhood_counts = defaultdict(int)
		columns = ["Location", "Parent", "Inspection Violation Count", "Color"]
		boston = ["Boston Area", '', 0, 0]
		data.append(columns)
		data.append(boston)
		for i, entry in enumerate(crm):
			if entry['city'] and entry['neighborhood']:
				#neighborhood_counts[entry['city']][entry['neighborhood']] += 1
				neighborhood_counts[entry['neighborhood']] += 1
		for neighborhood, count in neighborhood_counts.items():
			data.append([str(neighborhood), "Boston Area", count, 0])

	return render_to_response('tree_map.html',{'data':data}, context_instance=RequestContext(request))
"""