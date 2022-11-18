from django.shortcuts import render

def welcome_passenger(r):
    return render(r, "passenger/passenger_details.html")

