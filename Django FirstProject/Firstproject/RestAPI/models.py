from django.db import models


# Create your models here.
class userRegister(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
