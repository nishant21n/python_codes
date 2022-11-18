from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def accounts_welcome(r):
    return HttpResponse("<h1>  Welcome to ICICI Acounts </h1>")