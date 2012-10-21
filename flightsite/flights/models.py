from django.db import models

# Flight module holds flight level information
class Flight(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    distance = models.FloatField()
    flight_date = models.DateField('flight date')
    airline = models.CharField(max_length=50)
    
    # Cabin field includes choices
    F = 'Frst'
    Y = 'Ecnmy'
    cabin_choices = (
        (F, 'First Class'),
        (Y,'Economy'))
    cabin = models.CharField(max_length=20,
                            choices = cabin_choices,
                            default = Y)
    
    equipment = models.CharField(max_length=50)
    miles_redemption = models.BooleanField()

    def __unicode__(self):
        return self.origin + "-" + self.destination + " " + str(self.flight_date.month) + "/" +str(self.flight_date.day) +"/" + str(self.flight_date.year)


## To do, make equipment a choosable field https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.choices

