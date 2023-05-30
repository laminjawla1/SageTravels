from django.shortcuts import render
from .models import Flight, Passenger
from . forms import AddFlightForm, AddPassengerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    flights = Flight.objects.all()
    recent_flights = flights.order_by("-date")

    if request.method == 'POST':
        form = AddFlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Flight saved successfully")
        keyword = request.POST.get('flight_info')
        if keyword:
            flights = flights.filter(
                origin__city__icontains=keyword,
            ).all()
    return render(request, 'flights/index.html', {
        'flights': flights, 'recent_flights': recent_flights, 'form': AddFlightForm,
        'Keyword': 'Flight', 'keyword': 'flight_info'
    })

@login_required
def flight(request, flight_id):
    flight = None
    try:
        flight = Flight.objects.get(id=flight_id)
    except:
        messages.error(request, "No flights found")
    if request.method == "POST":
        passenger = request.POST.get('passenger')
        try:
            passenger = Passenger.objects.get(id=int(passenger))
        except:
            messages.error(request, "No passenger found")
            return HttpResponseRedirect(reverse('flight', args=(flight.id,)))
        passenger.flights.add(flight)
        messages.success(request, "Flight booked successfully")
    recent_flights = Flight.objects.order_by("-date")
    return render(request, 'flights/flight.html', {
        'flight': flight, 'recent_flights': recent_flights, 'Keyword': 'Flight',
        'passengers': flight.passengers.all(), 'form': AddPassengerForm,
        'non_passengers': Passenger.objects.exclude(flights=flight).all(),
        'total_passengers': len(flight.passengers.all()),
    })

@login_required
def passengers(request):
    passengers = Passenger.objects.all()
    recent_flights = Flight.objects.all().order_by("-date")
    if request.method == 'POST':
        form = AddPassengerForm(request.POST)
        if form.is_valid():
            form.save()
        keyword = request.POST.get('passenger')
        if keyword:
            passengers = passengers.filter(
                first_name__icontains=keyword,
            ).all()
    return render(request, 'flights/passengers.html', {
            'passengers': passengers, "recent_flights": recent_flights, 'form': AddPassengerForm,
            'Keyword': 'Passenger', 'keyword': 'passenger'
    })