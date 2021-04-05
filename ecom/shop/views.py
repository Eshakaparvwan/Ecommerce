from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
from math import ceil
def index(request):
    # products=Product.objects.all()
    # n=len(products)
   
    # nSlides=n
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n
        allProds.append([prod,range(1,nSlides),nSlides])


    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,"shop/search.html")
def productview(request,pid):
    product=Product.objects.filter(id=pid)
    print(product)
    return render(request,"shop/prodview.html",{'product':product[0] })
def checkout(request):
      return render(request,"shop/checkout.html")