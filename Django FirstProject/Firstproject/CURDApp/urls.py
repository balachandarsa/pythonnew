
from django.urls import path,include
from CURDApp import views

urlpatterns = [
    path('emp/', views.getEmployeeDetails),
    path('newemp/', views.getCreateNewEmployee),
    path('delemp/<id>', views.Delete_Employee),
    path('updateemp/<id>', views.Update_Employee),
    ]