from django.db import models

# Create your models here.
class DepartMent(models.Model):
    name = models.CharField(max_length=100,unique=True)
    pid = models.ForeignKey('self',related_name="child",on_delete=models.SET_NULL,null=True)

# Create your models here.
class Tusers(models.Model):  
    name = models.CharField(max_length=100, unique=True)
    passwd = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=50, unique=True)
    pic_url = models.CharField(max_length=100)
    tscore = models.IntegerField(default=0)
    lock_score = models.IntegerField(default=0)
    # avatar =models.CharField(max_length=200,default='')
  
    def __str__(self):  
        return self.name
    
    
#收费表 
class Fee(models.Model):  
    money = models.IntegerField(verbose_name='收费')  
    docker_types = models.IntegerField(choices=((1, '3甲'), (2, '普通')), verbose_name='医生类型')  
    types = models.IntegerField(choices=((1, '普通'), (2, '极速')), verbose_name='问诊类型')  
  
    class Meta:  
        verbose_name = '收费'  
        verbose_name_plural = '收费'  
  
    def __str__(self):  
        return f'收费{self.money}元'  

#患者表
class Patient(models.Model):  
    # 假设你的应用名称是 'myapp'  
    # 你需要在你的app的models.py文件中定义这个类  
  
    # 字段名: name, 类型: varchar(30), 中文名: 姓名  
    name = models.CharField(max_length=30, verbose_name='姓名')  
  
    # 字段名: code, 类型: varchar(50), 中文名: 身份证号, 唯一约束  
    code = models.CharField(max_length=50, unique=True, verbose_name='身份证号')  
  
    # 字段名: sex, 类型: int, 中文名: 性别  
    # 通常我们会使用一个CharField来存储性别，并设置选择项（例如：'M', 'F'），但这里为了简单起见，我们使用IntegerField  
    sex = models.IntegerField(verbose_name='性别')  # 你可以添加choices来限制可能的值  
  
    # 字段名: is_default, 类型: bool, 中文名: 是否默认  
    is_default = models.BooleanField(default=False, verbose_name='是否默认')  
  
    # 字段名: userid, 类型: int, 中文名: 用户id, 外键关联用户表  
    userid = models.ForeignKey(Tusers,on_delete=models.CASCADE)
  
    class Meta:  
        verbose_name = '用户信息'  
        verbose_name_plural = '用户信息列表'  
  
    def __str__(self):  
        return self.name
    

    
#订单表
class Orders(models.Model):  
    orderno = models.CharField(max_length=255,primary_key=True) 
    descrip = models.CharField(max_length=255, verbose_name='病情描述')  
    times = models.CharField(max_length=30, verbose_name='持续时间')  
    pic_url = models.CharField(max_length=200, verbose_name='文件')  
    is_into = models.BooleanField(default=False, verbose_name='是否就诊过')  
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name='患者id')  # 注意：这里通常使用外键关联Patient模型  
    userid = models.ForeignKey(Tusers,on_delete=models.CASCADE,verbose_name='用户id')  # 注意：这里通常使用外键关联User模型  
    status = models.IntegerField(choices=((1, '生成'), (2, '已支付'), (3, '支付失败')), verbose_name='订单状态')  
    transaction = models.CharField(max_length=50, verbose_name='流水号')  
    pay_type = models.IntegerField(choices=((1, '支付宝'), (2, '微信'), (3, '网银')), verbose_name='支付类型')  
    docker_types = models.IntegerField(choices=((1, '3甲'), (2, '普通')), verbose_name='医生类型')  
    types = models.IntegerField(choices=((1, '普通'), (2, '极速')), verbose_name='问诊类型')  
    department = models.ForeignKey(DepartMent, on_delete=models.CASCADE, verbose_name='科室id')  
    score = models.IntegerField(default=0)
    couponid = models.IntegerField(default=0)
    couponmoney = models.IntegerField(default=0)
    tmoney = models.IntegerField(default=0)
    pay_money = models.IntegerField(default=0)
    class Meta:  
        verbose_name = '咨询订单'  
        verbose_name_plural = '咨询订单'  
  
    def __str__(self):  
        return f'订单ID: {self.id}'
    
  
class Score(models.Model):  
    userid = models.ForeignKey(Tusers,on_delete=models.CASCADE)
    l_type = models.IntegerField(default=1,verbose_name='积分类型 1加  2减')
    score = models.IntegerField(default=0)
    
# #优惠券表
class Coupon(models.Model):
    name = models.CharField(max_length=50)  
    money = models.IntegerField(default=0)
    
# #优惠券表
class UserCoupon(models.Model):
    userid = models.ForeignKey(Tusers,on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  
    money = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    is_used = models.BooleanField(default=False)
    
class Doctor(models.Model):
    name = models.CharField(max_length=50)  
    mobile = models.CharField(max_length=11,unique=True)  
    deptid = models.ForeignKey(DepartMent,on_delete=models.CASCADE)
    
class PatientDoctor(models.Model):
    userid = models.ForeignKey(Tusers,on_delete=models.CASCADE,verbose_name='用户id')  # 注意：这里通常使用外键关联User模型 
    doctorid = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name='用户id') # 注意：这里通常使用外键关联User模型
    patient =  models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name='用户id')
    status = models.IntegerField(default=1)
    orderno = models.CharField(max_length=255)
    #加字段  处方  病例
    is_pay = models.BooleanField(default=False)
    pay_status = models.IntegerField(default=1) #1没支付  2支付成功  3支付失败
    pay_type = models.IntegerField(default=1)
    transaction_no = models.CharField(max_length=255,default='')
    money = models.IntegerField(default=0)
