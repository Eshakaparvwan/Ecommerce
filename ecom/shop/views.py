from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
from math import ceil
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4 + ceil((n/4) + (n//4))

    params={'no_of_slides':nSlides, 'range': range(nSlides),'product':products}
    return render(request,'shop/index2.html',params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("Contact")
def tracker(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("search")
def productview(request):
    return HttpResponse("prodView")
def checkout(request):
    return HttpResponse("checkout")