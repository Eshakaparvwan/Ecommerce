from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
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
    if request.method=="POST" :
        
        name=request.POST.get('name','')
        #print(name)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        # print(name,email,phone,email)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    
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
    thank=False
    if request.method=="POST" :
        itemsjson=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        #print(name)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        phone=request.POST.get('phone','')
        # print(name,email,phone,email)
        order=Orders(items_json=itemsjson,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank=True
        #id1=order.order_id
    return render(request,"shop/checkout.html",{'thank':thank})