from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'product': products, 'range': range(1, nSlides)}

    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


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
