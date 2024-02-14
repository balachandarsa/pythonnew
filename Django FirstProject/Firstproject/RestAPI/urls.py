
from django.urls import path,include
from RestAPI import views

urlpatterns = [
    path('getuser/', views.getUserDetails),
    path('postuser/', views.createUser),

    ]