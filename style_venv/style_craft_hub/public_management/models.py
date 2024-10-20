
from django.db import models
from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    name = models.CharField(max_length=50,default='')
    contact = models.IntegerField(null=True)
    address = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=50,default='')
    license = models.IntegerField(null=True)
    location = models.URLField(null=True)
    id_proof = models.FileField(null=True, upload_to='id_proof/')
    usertype = models.IntegerField(null=True,default=1)

class Product(models.Model):
    fabric = models.CharField(max_length=50,default='')
    measurement = models.IntegerField(null=True)
    style_preference = models.CharField(max_length=50,default='')
    fit_preference = models.CharField(max_length=50,default='')
    purpose_of_the_garment = models.IntegerField(null=True)
    timeline = models.URLField(null=True)
    image = models.FileField(null=True, upload_to='id_proof/')
    cost = models.IntegerField(null=True,default=1)