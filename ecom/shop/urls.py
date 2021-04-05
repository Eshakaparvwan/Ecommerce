"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index,name="shophome"),
    path('about/', views.about,name="Aboutus"),
    path('contact/', views.contact,name="contactus"),
    path('tracker/', views.tracker,name="trackingStatus"),
    path('products/<int:pid>', views.productview,name="productview"),
    path('checkout/', views.checkout,name="Checkout"),
    path('search', views.search,name="Search"),
    # path('', views.index,name="shophome"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

