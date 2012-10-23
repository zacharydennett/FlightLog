from django.db import models


# Flight module holds flight level information
class Flight(models.Model):
    origin = models.ForeignKey('Airport_list')
    # destination = models.ForeignKey('Airport_list')
    distance = models.FloatField()
    flight_date = models.DateField('flight date')
    airline = models.ForeignKey('Airline_list')
    
    # Cabin field includes choices
    cabin_choices = (('Cabin', (
                        ('first', 'First Class'),
                        ('business', 'Business Class'),
                        ('economy plus', 'Economy Plus Class'),
                        ('economy', 'Economy Class'),
                      )))
    cabin = models.CharField(max_length=20,
                            choices = cabin_choices[1],
                            default = cabin_choices[1][3]
                            )
    
    aircraft = models.ForeignKey('Aircraft_list')
    miles_redemption = models.BooleanField()
    def __unicode__(self):
        return self.origin + "-" + self.destination + " " + str(self.flight_date.month) + "/" +str(self.flight_date.day) +"/" + str(self.flight_date.year)


# This table is createds to define the choices of aircraft
class Aircraft_list(models.Model):
    aircraft_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.aircraft_name
    class Meta:
        ordering = ('aircraft_name',)

class Airport_list(models.Model):
    airport_code = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.airport_code + "-" + self.airport_name
    class Meta:
        ordering = ('airport_code',)

class Airline_list(models.Model):
    airline_name = models.CharField(max_length=100)
    airline_code = models.CharField(max_length=10)
    def __unicode__(self):
        return self.airline_code + "-" + self.airline_name
    class Meta:
        ordering = ('airline_name',)
    