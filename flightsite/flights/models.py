from django.db import models

# Flight module holds flight level information
class Flight(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    distance = models.FloatField()
    flight_date = models.DateTimeField('flight date')
    airline_code = models.CharField(max_length=3)
    cabin = models.CharField(max_length=20)
    equipment = models.CharField(max_length=50)
    miles_redemption = models.BooleanField()
    ## To do, make equipment a choosable field https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.choices
    
    def __unicode__(self):
        return self.origin + self.destination
