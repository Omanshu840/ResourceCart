from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("About Page")


def contact(request):
    return HttpResponse("Contact Page")


def tracker(request):
    return HttpResponse("Tracker Page")


def search(request):
    return HttpResponse("Search Page")


def productview(request):
    return HttpResponse("Product Page")


def checkout(request):
    return HttpResponse("Checkout Page")
