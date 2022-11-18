from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def account_welcome(r):
    return HttpResponse("<h1> Welcome to ICICI Accounts</h1><ul> <li>Current Account</li> <li>Saving Account</li></ul>")


def saving_account(r):
    return HttpResponse("<h1> Welcome to ICICI Saving Accounts</h1>")


def current_account(r):
    return HttpResponse("<h1> Welcome to ICICI Current Accounts</h1>")
