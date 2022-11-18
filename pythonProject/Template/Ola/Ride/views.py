from django.shortcuts import render

def welcome_rider(r):
    return render(r, "ride/rider_details.html")
