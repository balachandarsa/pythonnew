from django.shortcuts import render
from datetime import datetime


# Create your views here.
def Ipltables(request):
    date = datetime.now()
    details = {'year': '2024', 'name': 'TATA', 'country': 'India', 'date': date}
    return render(request, r'SecondWebApp/IplTable.html', context=details)

def Products(request):
    return render(request, r'SecondWebApp/ProductDetails.html')


def Prices(request):
    Keyboard = int(request.GET['Keyboard'])
    Laptop = int(request.GET['Laptop'])
    Mobile = int(request.GET['Mobile'])
    Mouse = int(request.GET['Mouse'])
    Tablet = int(request.GET['Tablet'])

    totalprice = Keyboard + Laptop + Mobile + Mouse + Tablet

    finalprice = {'price': totalprice}
    return render(request, r'SecondWebApp/Total-price.html', context=finalprice)


