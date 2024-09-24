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