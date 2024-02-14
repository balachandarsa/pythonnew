from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def Homepage(request):
    return render(request, r'FirstWebApp\Homepage.html')

def Register(request):
    return render(request, r'FirstWebApp\Register.html')

def Login(request):
    return render(request, r'FirstWebApp\Login.html')
