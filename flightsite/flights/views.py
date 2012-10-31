# Create your views here.
from django.http import HttpResponse
from flights.models import Flight
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm ## for the form stuff


def index(request):
#return HttpResponse("Hello World! This text comes from fligts/views index"):
    latest_flight_list = Flight.objects.order_by('-flight_date')[:50]
    template = loader.get_template('flights/index.html')
    context = Context({
                      'latest_flight_list': latest_flight_list,
                      })
    return HttpResponse(template.render(context))


def detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/detail.html', {'flight': flight})

def newflight(request):
    return HttpResponse("Hello, world. You're entering a new flight.")
