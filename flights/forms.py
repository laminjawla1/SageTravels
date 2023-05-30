from django import forms
from .models import Flight, Passenger

class AddFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['airline', 'origin', 'destination', 'duration', 'seats_available', 'price']

class AddPassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name']