from django.shortcuts import render

# Create your views here.


def mobile_items(r):
    md = {"S": "Samsung", "I": "Iphone", "N": "Nokia"}
    return render(r, "mobiles/mobiles.html", context=md)

