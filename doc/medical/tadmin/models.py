from django.db import models

# Create your models here.
class TestRole(models.Model):
    name = models.CharField(max_length=30,unique=True)
    
    class Meta:  
        verbose_name = '测试角色表'  
        verbose_name_plural = '测试角色表'  
        db_table = "testrole"
        


class Resource(models.Model):
    name = models.CharField(max_length=30,unique=True)
    pid = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    url = models.CharField(max_length=100)
    
    class Meta:  
        verbose_name = '资源表'  
        verbose_name_plural = '资源表'  
        db_table = "resource"
        
class Roles(models.Model):
    name = models.CharField(max_length=30,unique=True)
    pid = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    resource = models.ManyToManyField(Resource)
    
    class Meta:  
        verbose_name = '角色表'  
        verbose_name_plural = '角色表'  
        db_table = "roles"
        
        
class AdminUser(models.Model):
    name = models.CharField(max_length=30,unique=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    class Meta:  
        verbose_name = '用户表'  
        verbose_name_plural = '用户表'  
        db_table = "admin_user"  
        
        
class ResourceInterface(models.Model):
    resid = models.ForeignKey(Resource,on_delete=models.SET_NULL,null=True,related_name='interface')
    url = models.CharField(max_length=100)
    
    class Meta:  
        verbose_name = '接口权限表'  
        verbose_name_plural = '接口权限表'  
        db_table = "resource_interface"  

