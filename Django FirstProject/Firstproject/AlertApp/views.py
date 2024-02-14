from django.contrib import messages
from django.shortcuts import render


# Create your views here.
def AlertMessage(request):
    return render(request, "AlertApp/Alert.html")


def success(request):
    messages.success(request, "This is a Alert page")
    return render(request, "AlertApp/Alert.html")


def error(request):
    messages.error(request, "This is a error page")
    return render(request, "AlertApp/Alert.html")


def Info(request):
    messages.info(request, "This is a Information message")
    return render(request, "AlertApp/Alert.html")


def Warning(request):
    messages.warning(request, "This is a Warning message")
    return render(request, "AlertApp/Alert.html")
