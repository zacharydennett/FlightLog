## from http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/

import math

def distance(lat1, lon1, lat2, lon2):
    #radius = 6371 # km
    radius = 3958.76 #miles
    
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    
    return d