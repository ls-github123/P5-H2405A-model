from django.db import models

# Create your models here.
class Testmodel(models.Model):
    name = models.CharField(max_length=50)  
    mobile = models.CharField(max_length=11,unique=True)  


class Torders(models.Model):
    orderno = models.CharField(max_length=50)  
    descip = models.CharField(max_length=200)  