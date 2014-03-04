from geopy import geocoders 
from broken_windows.settings import GOOGLE_MAPS_API_KEY

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
      g = geocoders.GoogleV3()#api_key=GOOGLE_MAPS_API_KEY)
      place, (lat, lng) = g.geocode(address)
      res['latitude'] = lat
      res['longitude'] = lng
      return res
    except Exception as e:
      print "%s , %s"%(e,address)
    return None



