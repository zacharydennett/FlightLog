from django.db import models
from flights.greatcircle import distance
import math

class Airport_list(models.Model):
    airport_code = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=200)
    country = models.CharField(max_length = 100)
    US_state = models.CharField(blank=True, max_length=100)
    long_deg = models.IntegerField()
    long_min = models.IntegerField()
    long_sec = models.IntegerField()
    long_ew = models.CharField(max_length = 1)
    lat_deg = models.IntegerField()
    lat_min = models.IntegerField()
    lat_sec = models.IntegerField()
    lat_ns = models.CharField(max_length = 1)
    def __unicode__(self):
        return self.airport_code
    def longitude(self):
        if self.long_ew == "E":
            r = 1.00 * self.long_deg + self.long_min / 60.0 + self.long_sec / (60.0 * 60.0)
        else:
            r = -1.00 * (self.long_deg + self.long_min / 60.0 + self.long_sec / (60.0 * 60.0))
        return r
    def latitude(self):
        if self.lat_ns == "N":
                r = 1.00 * self.lat_deg + self.lat_min / 60.0 + self.lat_sec / (60.0 * 60.0)
        else:
                r = -1.00 * (self.lat_deg + self.lat_min / 60.0 + self.lat_sec / (60.0 * 60.0))
        return r  
    class Meta:
        ordering = ('airport_code',)


# Flight module holds flight level information
class Flight(models.Model):
    origin = models.ForeignKey(Airport_list, related_name = "origin_key")
    destination = models.ForeignKey(Airport_list, related_name = "destination_key")
    flight_date = models.DateField('flight date')
    airline = models.ForeignKey('Airline_list')
    cabin_choices = (('Cabin', (
                        ('first', 'First Class'),
                        ('business', 'Business Class'),
                        ('economy plus', 'Economy Plus Class'),
                        ('economy', 'Economy Class'),
                      )))
    cabin = models.CharField(max_length=20, choices = cabin_choices[1],default = cabin_choices[1][3])
    aircraft = models.ForeignKey('Aircraft_list')
    miles_redemption = models.BooleanField()
    def __unicode__(self):
        return str(self.origin) + "-" + str(self.destination) + " " + str(self.flight_date.month) + "/" +str(self.flight_date.day) +"/" + str(self.flight_date.year) + " " + str(round(self.distance(),1)) + "miles"
    def distance(self):
        # Calculated the great cirlce distance. Based on code found here: http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/
        lat1 = self.origin.latitude()
        lon1 = self.origin.longitude()
        lat2 = self.destination.latitude()
        lon2 = self.destination.longitude()
        radius = 3958.76 #miles
    
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
    #return self.origin.longitude + self.destination.longitude ## TO DO make this actually calculate distance!


class Aircraft_list(models.Model):
    aircraft_name = models.CharField(max_length=30)
    manufacturer =models.CharField(max_length = 100)
    def __unicode__(self):
        return str(self.manufacturer) +" "+str(self.aircraft_name)
    class Meta:
        ordering = ('aircraft_name',)


class Airline_list(models.Model):
    airline_code = models.CharField(max_length=10)
    airline_name = models.CharField(max_length=100)
    airline_country = models.CharField(max_length=100)
    def __unicode__(self):
        return self.airline_code + "-" + self.airline_name
    class Meta:
        ordering = ('airline_name',)
    