
from django.urls import path,include
from FormsWebApp import views

urlpatterns = [
    path('register/', views.Registration),
    path('set/', views.getRegisterModels),

    ]