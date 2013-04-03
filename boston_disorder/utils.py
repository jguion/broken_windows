from geopy import geocoders
"""
def save_crime_from_json(data):
    for crime_list in data:
        c = Crime(compnos = crime_list[8],
                  suppnos = crime_list[9],
                  reportingarea = crime_list[10],
                  incident_type_description = crime_list[11],
                  crime_code = crime_list[12],
                  crimecode_description = crime_list[13],
                  finalcrimecode = crime_list[14],
                  finalcrimecode_desc = crime_list[15],
                  reptdistrict = crime_list[16],
                  fromdate = crime_list[17],
                  todate = crime_list[18],
                  weapontype = crime_list[19],
                  buildingtype = crime_list[20],
                  placeofentry = crime_list[21],
                  perpetratorsnos = crime_list[22],
                  suspecttransportation = crime_list[23],
                  victimactivity = crime_list[24],
                  unusualactivity = crime_list[25],
                  weather = crime_list[26],
                  neighborhood = crime_list[27],
                  lighting = crime_list[28],
                  clearancestatusdesc = crime_list[29],
                  main_crimecode = crime_list[30],
                  robbery_type = crime_list[31],
                  robbery_attempt = crime_list[32],
                  burglary_time = crime_list[33],
                  domestic = crime_list[34],
                  weapon_type = crime_list[35],
                  shift = crime_list[36],
                  day_week = crime_list[37],
                  ucrpart = crime_list[38],
                  location = crime_list[39],
                  x = crime_list[40],
                  y = crime_list[41],
                  score = crime_list[42],
                  greporting = crime_list[43],
                  gsector = crime_list[44],
                  gbeat = crime_list[45],
                  gdistrict = crime_list[46],
                  shooting_type = crime_list[47],
                  computedcrimecode = crime_list[48],
                  computedcrimedesc = crime_list[49],
                  location_1 = crime_list[50])
        c.save()
        print "Save Successful"

def save_service_request_from_json(data):
    for i, service_request_list in enumerate(data):
        c = ServiceRequest(
                case_enquiry_id = service_request_list[8],
                open_dt = service_request_list[9],
                closed_dt = service_request_list[10],
                case_status = service_request_list[11],
                closure_reason = service_request_list[12],
                case_title = service_request_list[13],
                subject = service_request_list[14],
                reason = service_request_list[15],
                type = service_request_list[16],
                queue = service_request_list[17],
                department = service_request_list[18],
                location = service_request_list[19],
                fire_district = service_request_list[20],
                pwd_district = service_request_list[21],
                city_council_district = service_request_list[22],
                police_district = service_request_list[23],
                neighborhood = service_request_list[24],
                neighborhood_services_district = service_request_list[25],
                ward = service_request_list[26],
                precinct = service_request_list[27],
                land_usage = service_request_list[28],
                location_street_name = service_request_list[29],
                location_zipcode = service_request_list[30],
                location_x = service_request_list[31],
                location_y = service_request_list[32],
                source = service_request_list[33],
                geocoded_loc = service_request_list[34])
        c.save()
        print "Save Successful %s"%i
"""
def parse_lat_lng(l):
    l = l.split(',')
    lat = None
    lng = None
    address = None
    res = {}
    if len(l) == 5: 
      lat = l[1]
      lng = l[2]
    elif len(l) == 8:
      lat = l[4]
      lng = l[5]
      street = l[0][15:-1]
      city = l[1][8:-1]
      state = l[2][9:-1]
      address = "%s, %s %s"%(street,city,state)
      #zipcode = l[3]
    try:
      if lat == "None":
        return None
      #print "*** %s, %s"%(lat[2:],lng)
      lat = float(lat[3:-1])
      lng = float(lng[3:-1])
      #print "%s, %s"%(lat,lng) 
      res['latitude'] = lat
      res['longitude'] = lng
      #res = {'latitude':lat, 'longitude': lng}
      return res
    except Exception as e:
      if address != None:
        return get_lat_long(address)
    return None

def get_lat_long(address):
    res = {}
    try:
      g = geocoders.Google()
      place, (lat, lng) = g.geocode(address)
      res['latitude'] = lat
      res['longitude'] = lng
      return res
    except Exception as e:
      print e
    return None



