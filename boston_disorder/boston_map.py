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

class BostonMap:
	#data_type : either "crm" or "cad"
	#map_type : ex "housing" or "guns"
	def __init__(self, request, data_type, map_type, use_addresses=False):
		self.map_type = map_type
		self.use_addresses = use_addresses
		filter_args = {}
		#Get any filter arguements from the url query string
		for key, item in request.GET.items():
			if key.startswith('f_'):
				if key.endswith("__in") and item.startswith("list("):
					item = [x.strip() for x in item[5:-1].split(",")]
				filter_args[key[2:]] = item
		self.filter_args = filter_args


		dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else None
		self.dthandler = dthandler

		self.show_details = request.GET.get('show_details', False)


		#Determine data granularity (ex Block Group)
		if request.GET.get('granularity'):
			granularity = request.GET.get('granularity')
			is_default = False
		else:
			granularity = "Block Group"
			is_default = True
		self.granularity = granularity
		self.is_default = is_default

		area_identifier = None
		if granularity == "Census Tract":
			area_identifier ='ct_id'
		elif granularity == "Block Group":
			area_identifier = 'bg_id'
		elif granularity == "Block":
			area_identifier = 'blk_id'
		self.area_identifier =area_identifier

		#dictionary of area identifiers to lat & long
		self.blocks_to_coordinates = (dict((x['areaid'], x) for x in
								TigerData.objects.filter(type=self.granularity)
								.values("areaid", "latitude", "longitude")))

		#Initialize dictionary of addresses to lat & long
		self.address_to_coordinates = None

		#Find population and area of block groups
		self.bg_population = (dict((x['bg_id'], (x['totalpop'], x['popden'], x['area'])) for x in (BostonBlockGroup.objects
													.values("totalpop", "bg_id", "popden", "area"))))


		#Determine filter for the selected map type
		map_filter = FILTER_DICT.get(map_type)
		self.display_type = TYPE_DISPLAY_NAMES.get(map_type)
		self.crm = []
		self.cad = []
		#populated selected data model and apply all relevent filters
		if data_type == "crm":
			crm = (BostonCRM.objects.filter(**filter_args) if filter_args else BostonCRM.objects)
			self.crm = (crm.filter(type__in=map_filter)
						   .values('location', 'city', 'state', 'open_dt', 'reason', 'subject',
						   		   'type', 'nsa_name', 'bg_id', 'blk_id', 'ct_id'))
		elif data_type == "cad":
			if type(map_filter) == dict:
				cad = Boston911Calls.objects.filter(**map_filter)
			else:
				cad = Boston911Calls.objects.filter(map_filter)

			if filter_args: 
				cad = cad.filter(**filter_args)
			self.cad = cad

	#Gets the area id given a granularity and item
	def get_areaid(self, x):
		remove_block_group = lambda x:x[:12]+x[13:]
		if self.granularity == "Census Tract":
			return str(x['ct_id'])
		elif self.granularity == "Block Group":
			return str(x['bg_id'])
		elif self.granularity == "Block":
			return remove_block_group(str(x['blk_id']))
		else:
			return None

	# gets the coordinates of an item
	def get_coordinates(self, x):
		areaid = self.get_areaid(x)
		return self.blocks_to_coordinates.get(areaid) if areaid else None

	#Gets a list of dictionarys of information from each crm row
	#used to populate address level information / additional details
	def get_crm_data(self):
		locations = []
		for i, entry in enumerate(self.crm):
			res = {}
			areaid = self.get_areaid(entry)		
			address = "%s, %s, %s"%(entry['location'], entry['city'], entry['state'])
			address_coordinate = None
			if self.use_addresses and self.is_default or not areaid:
				if self.address_to_coordinates is None:
					self.address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
				address_coordinates = self.address_to_coordinates.get(address)
				res['address_latitude'] = float(address_coordinates['latitude']) if address_coordinates else None
				res['address_longitude'] = float(address_coordinates['longitude']) if address_coordinates else None
	
			if areaid: 
				coordinates = self.blocks_to_coordinates.get(areaid)
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
		if self.use_addresses:
			locations = sorted(locations, key=lambda x: (x['date']))
		else:
			locations = sorted(locations, key=lambda x: (x['address'], x['date']))
		return locations
				
	#Gets a list of dictionaries of information from each area group
	#Used to create heatmap.
	def get_crm_areas(self):
		areas = ([{"areaid":info[self.area_identifier],
				   "nsa_name":info['nsa_name'], 
				   "count":info['pk__count'],
		   		   "coordinates":self.get_coordinates(info), 
		   		   "pop":self.bg_population.get(info['bg_id'])[0], 
		   		   "popden":self.bg_population.get(info['bg_id'])[1], 
		   		   "area":self.bg_population.get(info['bg_id'])[2]} 
		   		  	for info in self.crm.values(self.area_identifier)
		   		  				   .distinct()
		   		  				   .annotate(Count('pk'))
								   .values("nsa_name","pk__count",self.area_identifier, 'bg_id')
								   .order_by('-pk__count')
						  if info[self.area_identifier] is not None]
					if self.area_identifier else [])
		return areas

	#Gets a list of dictionarys of information from each cad row
	#used to populate address level information / additional details
	def get_cad_locations(self):
		locations = []
		for i, entry in enumerate(self.cad.values()):
			res = {}
			address = "%s"%(entry['match_text'])
			areaid = self.get_areaid(entry)

			if self.is_default:
				if self.address_to_coordinates is None:
					self.address_to_coordinates = (dict((x['address'], x) for x in 
									AddressLatLog.objects.values("address", "latitude", "longitude")))
				address_coordinates = self.address_to_coordinates.get(address)
				res['address_latitude'] = float(address_coordinates['latitude']) if address_coordinates else None
				res['address_longitude'] = float(address_coordinates['longitude']) if address_coordinates else None

			if areaid: 
				coordinates = self.blocks_to_coordinates.get(areaid)
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
		return locations

	#Gets a list of dictionaries of information from each area group
	#Used to create heatmap.
	def get_cad_areas(self):
		areas = ([{"areaid":info[self.area_identifier],
				   "nsa_name":info['nsa_name'], 
				   "count":info['pk__count'],
				   "coordinates":self.get_coordinates(info), 
				   "pop":self.bg_population.get(info['bg_id'])[0], 
				   "popden":self.bg_population.get(info['bg_id'])[1], 
				   "area":self.bg_population.get(info['bg_id'])[2]} 
				 for info in self.cad.values(self.area_identifier)
				 				  .distinct()
				 				  .annotate(Count('pk'))
								  .values("nsa_name","pk__count",self.area_identifier, 'bg_id')
								  .order_by('-pk__count')
						if info[self.area_identifier] is not None]
					if self.area_identifier else [])
		return areas



