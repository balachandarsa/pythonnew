from django.contrib import admin
from django.urls import path, include
from SecondWebApp import views as v2

urlpatterns = [
    path('iptables/', v2.Ipltables),
    path('products/', v2.Products),
    path('prices/', v2.Prices),
    ]