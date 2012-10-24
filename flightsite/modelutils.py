import flights.models
from django.db import connection

def add_aircraft(plane, mnf):
    a = Aircraft_list(aircraft_name = plane, manufacturer = mnf)
    a.save


add_aircraft('777', 'Boeing')