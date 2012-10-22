from django.contrib import admin
from flights.models import Flight, Aircraft_list, Airport_list, Airline_list

admin.site.register(Flight)
admin.site.register(Aircraft_list)
admin.site.register(Airport_list)
admin.site.register(Airline_list)