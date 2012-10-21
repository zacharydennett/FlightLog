from django.db import models

# Flight module holds flight level information
class Flight(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    flight_date = models.DateTimeField('flight date')
    airline_code = models.CharField(max_length=3)
    cabin = models.CharField(max_length=20)
    equipment = models.CharField(max_length=50)('aircraft type')
    miles_redemption = modles.binary
