from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def credit_welcome(r):
    return HttpResponse("<h1> Welcome to ICICI Credit Cards</h1><ul> <li>Silver Credit Card</li> <li>Platinum Credit Card</li></ul>")


def silver_credit_card(r):
    return HttpResponse("<h1> Welcome to ICICI Silver Credit Cards</h1>")


def platinum_credit_cards(r):
    return HttpResponse("<h1> Welcome to ICICI Platinum Credit Cards</h1>")
