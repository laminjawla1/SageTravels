from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flight/<int:flight_id>/view", views.flight, name="flight"),
    path("passengers/", views.passengers, name="passengers")
]