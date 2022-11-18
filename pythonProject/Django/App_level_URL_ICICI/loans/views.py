from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def loan_welcome(r):
    return HttpResponse("<h1> Welcome to ICICI Loans</h1><ul> <li>Personal Loans</li> <li>Home Loans</li></ul>")


def personal_loan(r):
    return HttpResponse("<h1> Welcome to ICICI Personal Loans</h1>")


def home_loans(r):
    return HttpResponse("<h1> Welcome to ICICI Home Loans</h1>")
