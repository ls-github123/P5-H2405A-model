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
    numbers = models.IntegerField()
    userid = models.IntegerField()
    
    
class Questions(models.Model):
    ask = models.CharField(max_length=50,null=True,blank=True) 
    answer = models.TextField(default='') 
    add_time = models.DateTimeField(auto_now_add=True)
    cid = models.ForeignKey(Cates,on_delete=models.CASCADE,related_name='questions')
    
    
#用户表 id mobile nikename addtime
#三方登录表   id  userid(外键用户表) uid(钉钉uid) types()
#订单表 id money  addtime  pay_status  userid(外键关联用户表)
#订单详情表   id  orderno(外键关联订单表) gid gname  comment_status
#评价表   id  userid  message  level  gid

class Author(models.Model):
    author_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='author_id')

    def __str__(self):
        return self.title
    
    
class Goods(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sales = models.IntegerField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Resource(models.Model):
    name = models.CharField(max_length=200,unique=True)
    pid = models.ForeignKey('self',null=True,blank=True,on_delete = models.SET_NULL)
    url = models.CharField(max_length=200,default="")
    # customer = models.ManyToManyField(Customer,related_name='resource')
    
    def __str__(self):
        return self.name  

class Roles(models.Model):
    name = models.CharField(max_length=200,unique=True)
    resources = models.ManyToManyField(Resource)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    account = models.CharField(max_length=200,unique=True)
    roles = models.ForeignKey(Roles,on_delete=models.SET_NULL,null=True,blank=True)
   

    def __str__(self):
        return self.name
    

    
    
