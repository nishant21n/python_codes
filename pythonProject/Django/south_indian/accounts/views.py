from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saving_accounts(r):
    return HttpResponse("<h1>Welcome to Saving Accounts</h1>")
