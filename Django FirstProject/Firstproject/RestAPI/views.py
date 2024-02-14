from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import userRegister
from .serializers import userRegisterSerializer


# Create your views here.
@api_view(["GET"])
def getUserDetails(request):
    user = userRegister.objects.all()
    serializers = userRegisterSerializer(user, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def createUser(request):
    newuser = userRegisterSerializer(data=request.data)
    if newuser.is_valid():
        newuser.save()
    return Response(newuser.data)
