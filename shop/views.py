from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for item in cats:
        prod = Product.objects.filter(category=item)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Contact Page")


def tracker(request):
    return HttpResponse("Tracker Page")


def search(request):
    return HttpResponse("Search Page")


def productview(request, myid):

    product = Product.objects.filter(id=myid)

    return render(request, 'shop/product.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("Checkout Page")
