# Create your views here.
from django.http import HttpResponse
from flights.models import Flight
from django.template import Context, loader


def index(request):
#return HttpResponse("Hello World! This text comes from fligts/views index"):
    latest_flight_list = Flight.objects.order_by('-flight_date')[:5]
    template = loader.get_template('flights/index.html')
    context = Context({
                      'latest_flight_list': latest_flight_list,
                      })
    return HttpResponse(template.render(context))


def detail(request, flight_id):
    return HttpResponse("You're looking at flight %s." % flight_id)

