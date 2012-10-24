from flights.models import Aircraft_list

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

#print plane
#a = models.Aircraft_list(aircraft_name = plane, amnf)
#a.save


# add_aircraft('777', 'Boeing')