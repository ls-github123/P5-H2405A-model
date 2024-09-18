from django.db import models

# Create your models here.
class Testmodel(models.Model):
    name = models.CharField(max_length=50)  
    mobile = models.CharField(max_length=11,unique=True)  
  