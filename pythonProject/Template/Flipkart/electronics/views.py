from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def electronic_items(r):
    electronics_dict = {"S": "Samsung", "L": "LG", "I": "IFB"}
    return render(r, "electronics/electronics.html", context=electronics_dict)
