from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def show(r):
    return HttpResponse('<h1> Welcome to Loans</h1>')