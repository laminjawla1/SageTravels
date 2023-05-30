from django.contrib import admin
from . models import Flight, Airport, Airline, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination', 'duration', 'airline', 'seats_available', 'price', 'date']
    search_fields = ['origin__city', 'destination__city', 'airline__name']
admin.site.register(Flight, FlightAdmin)

class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'country']
    search_fields = ['code', 'city', 'country']
admin.site.register(Airport, AirportAdmin)

class AirlineAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
admin.site.register(Airline, AirlineAdmin)

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ['flights']
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
admin.site.register(Passenger, PassengerAdmin)