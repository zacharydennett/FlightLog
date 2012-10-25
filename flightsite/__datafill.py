from flights.models import Aircraft_list
from flights.models import Airline_list

def add_aircraft():
    a = Aircraft_list(aircraft_name = '737', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = '747', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = '757', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = '767', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = '777', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = '787', manufacturer = 'Beoing')
    a.save()
    a = Aircraft_list(aircraft_name = 'A319', manufacturer = 'Airbus')
    a.save()
    a = Aircraft_list(aircraft_name = 'A320', manufacturer = 'Airbus')
    a.save()
    a = Aircraft_list(aircraft_name = 'A321', manufacturer = 'Airbus')
    a.save()
    a = Aircraft_list(aircraft_name = 'A330', manufacturer = 'Airbus')
    a.save()
    a = Aircraft_list(aircraft_name = 'A340', manufacturer = 'Airbus')
    a.save()
    a = Aircraft_list(aircraft_name = 'A380', manufacturer = 'Airbus')
    a.save()


def add_airline():
    Airline_list(airline_code = 'AA', airline_name = 'American Airlines', airline_country = 'United States').save()
    Airline_list(airline_code = 'DL', airline_name = 'Delta Airlines', airline_country = 'United States').save()
    Airline_list(airline_code = 'UA', airline_name = 'United Airlines', airline_country = 'United States').save()
    Airline_list(airline_code = 'WN', airline_name = 'Southwest Airlines', airline_country = 'United States').save()