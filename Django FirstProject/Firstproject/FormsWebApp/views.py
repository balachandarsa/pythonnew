from django.http import HttpResponse
from django.shortcuts import render
from .import forms
from .models import RegisterModels


# Create your views here.

def Registration(request):
    form = forms.RegisterForms()
    return render(request, r'FormsWebApp/Register.html', context={"form": form})


def getRegisterModels(request):
    if request.method == 'POST':
        if request.POST.get('Firstname' and request.POST.get('Lastname') and request.POST.get('Email')
                            and request.POST.get('Password') and request.POST.get('Confirm_Password')):
            reg = RegisterModels()
            reg.Firstname = request.POST.get('Firstname')
            reg.Lastname = request.POST.get('Lastname')
            reg.Email = request.POST.get('Email')
            reg.Password = request.POST.get('Password')
            reg.Confirm_Password = request.POST.get('Confirm_Password')
            reg.save()
            return HttpResponse('success')
        else:
            return HttpResponse('unsuccessful')

    form = forms.RegisterForms()
    return render(request, r'FormsWebApp/Register.html', context={"form": form})
