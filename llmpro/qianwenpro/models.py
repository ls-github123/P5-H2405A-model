from django.db import models

# Create your models here.
class Testmodel(models.Model):
    name = models.CharField(max_length=50)  
    mobile = models.CharField(max_length=11,unique=True)  


class Torders(models.Model):
    orderno = models.CharField(max_length=50)  
    descip = models.CharField(max_length=200)  
    
    
class Cates(models.Model):
    # code = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=50,null=True,blank=True)  
    add_time = models.DateTimeField(auto_now_add=True)
    
    
class Questions(models.Model):
    ask = models.CharField(max_length=50,null=True,blank=True) 
    answer = models.CharField(max_length=50,null=True,blank=True)  
    add_time = models.DateTimeField(auto_now_add=True)
    cid = models.ForeignKey(Cates,on_delete=models.CASCADE,related_name='questions')