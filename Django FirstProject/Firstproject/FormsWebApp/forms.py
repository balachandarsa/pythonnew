from django import forms


class RegisterForms(forms.Form):
    Firstname = forms.CharField(max_length=20)
    Lastname = forms.CharField(max_length=20)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=12)
    Confirm_Password = forms.CharField(max_length=12)
