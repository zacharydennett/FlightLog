
from django.http import HttpResponse
from flights.models import Flight
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
## for the form stuff
from django.forms import ModelForm 
from django.forms.models import modelformset_factory


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
    FlightFormSet = modelformset_factory(Flight)
    if request.method == 'POST':
        formset = FlightFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
            return HttpResponse("IT WORKED!!!")
    else:
        formset = FlightFormSet()
    return render_to_response("flights/newflightpage.html", {
            "formset": formset,
    })


