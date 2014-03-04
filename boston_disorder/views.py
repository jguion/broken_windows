from django.shortcuts import render_to_response
from django.template import RequestContext

from boston_disorder.models import *
from boston_disorder.boston_map import BostonMap
import simplejson as json


## Physical disorder view using data from the CRM database
def crm(request, map_type=None):
	boston_map = BostonMap(request, data_type="crm", map_type=map_type, use_addresses=True)
	locations = boston_map.get_crm_data()
	areas = boston_map.get_crm_areas()

	data = json.dumps({'locations':locations,'area_info':areas,'map_type':'heat_map','show_addresses':True,
					   'show_details':boston_map.show_details, 'granularity':boston_map.granularity, 
					   'area_identifier':boston_map.area_identifier, 'is_default':boston_map.is_default},
					    default=boston_map.dthandler)

	return render_to_response('map.html',
							 {'data':data},
							  context_instance=RequestContext(request))

## Physical disorder view using data from the CRM database
## All address level information is hidden and never displayed
def limited_crm(request, map_type=None):
	boston_map = BostonMap(request, data_type="crm", map_type=map_type)
	locations = boston_map.get_crm_data()
	areas = boston_map.get_crm_areas()

	data = json.dumps({'locations':locations,'area_info':areas, 'map_type':'heat_map','show_addresses':False,
					   'show_details':boston_map.show_details, 'granularity':boston_map.granularity, 
					   'area_identifier':boston_map.area_identifier, 'is_default':boston_map.is_default},
					    default=boston_map.dthandler)

	return render_to_response('map.html',
							 {'data':data},
							  context_instance=RequestContext(request))

## Social disorder view using data from the CAD database
def calls(request, map_type=None):
	boston_map = BostonMap(request, data_type="cad", map_type=map_type, use_addresses=True)
	locations = boston_map.get_cad_locations()
	areas = boston_map.get_cad_areas()

	data = json.dumps({'locations':locations,'area_info':areas,'map_type':'heat_map','show_addresses':True,
						   'show_details':boston_map.show_details, 'granularity':boston_map.granularity, 
						   'area_identifier':boston_map.area_identifier, 'is_default':boston_map.is_default},
						    default=boston_map.dthandler)

	return render_to_response('map.html',
							 {'data':data},
							  context_instance=RequestContext(request))

## Social disorder view using data from the CAD database
## All address level information is hidden and never displayed
def limited_calls(request, map_type=None):
	boston_map = BostonMap(request, data_type="cad", map_type=map_type)
	locations = boston_map.get_cad_locations()
	areas = boston_map.get_cad_areas()

	data = json.dumps({'locations':locations,'area_info':areas, 'map_type':'heat_map','show_addresses':False,
					   'show_details':boston_map.show_details, 'granularity':boston_map.granularity, 
					   'area_identifier':boston_map.area_identifier, 'is_default':boston_map.is_default},
					    default=boston_map.dthandler)

	return render_to_response('map.html',
							 {'data':data},
							 context_instance=RequestContext(request))

# URL with information about the types of disorder
def more_info(request):
	return render_to_response('more_info.html',{}, context_instance=RequestContext(request))

