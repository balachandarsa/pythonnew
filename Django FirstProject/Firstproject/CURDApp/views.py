from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import EmployeeRegisterForm
from .models import EmployeeRegister


# Create your views here.
def getEmployeeDetails(request):
    empDetails = EmployeeRegister.objects.all()
    return render(request, "CURDApp/empdetails.html", context={"empDetails": empDetails})


def getCreateNewEmployee(request):
    form = EmployeeRegisterForm()
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "CURDApp/AddEmpDetails.html", context={"form": form})


def Delete_Employee(request, id):
    empdetails = EmployeeRegister.objects.get(id=id)
    empdetails.delete()
    # return HttpResponse(
    #    'Employee data deleted sucessfully <h1><a href="/curd/emp">click here to view the page</a></h1>')#
    return redirect("/curd/emp")


def Update_Employee(request, id):
    empdetails = EmployeeRegister.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST, instance=empdetails)
        if form.is_valid():
            form.save()
            return HttpResponse('Employee data deleted successfully <h1><a href="/curd/emp">click here to view the '
                                'page</a></h1>')
    return render(request, "CURDApp/UpdateEmp.html", context={"empdetails": empdetails})
