from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def credit_cards_welcome(r):
    return HttpResponse("<h1>  Welcome to ICICI Credit Cards </h1>")