
from django.urls import path,include
from AlertApp import views


urlpatterns = [
    path('msg/', views.AlertMessage, ),
    path('success/', views.success, name='Success'),
    path('error/', views.error, name='Error'),
    path('info/', views.Info, name='Info'),
    path('warning/', views.Warning, name='Warn'),
    ]