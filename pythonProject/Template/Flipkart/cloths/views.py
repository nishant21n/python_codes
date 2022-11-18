from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cloth_items(r):
    cloths_dict = {"M": "Men", "W": "Women", "K": "Kids"}
    return render(r, "cloths/cloths.html", context=cloths_dict)


def kids(r):
    return render(r, "cloths/cat/kids.html")


def men(r):
    return render(r, "cloths/cat/men.html")


def women(r):
    return render(r, "cloths/cat/women.html")

