### 1.rbac

~~~
acl基于用户的权限管理
rbac基于角色的权限管理
abac基于属性的权限管理

有四张表
管理员表
id   username   password    roleid   is_valid
1    zhangsan   123456         3        0
2    xiaozhang   345345        2        0

角色表
id  name
1    审核员
2    编辑员
3    财务

资源表
id  name      pid
1   商品管理    0
2   内容管理    0
3   统计管理    0
4   视频审核    2
5   添加商品    1
6   统计模块    3
7   长视频管理   2
8   短视频管理   2

角色资源表
roleid resid
3        4
3        5
1        6



~~~



2.流程

角色管理

![image-20230331095415756](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20230331095415756.png)

添加用户，选择角色

![image-20230331095740644](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20230331095740644.png)



~~~
角色：销售   4个资源  用户管理、角色管理、资源管理、财务管理

添加一个用户小明，小明属于销售角色
小明登录：
权限管理
   用户管理
   角色管理
   资源管理
财务模块
   财务管理
   
   
   select res.id,res.name,pres.id,pres.name from resources_roles as rr inner join resources as res on rr.resource_id=res.id  left join resources as pres on pres.id=res.pid where rr.roles_id=1;
~~~

~~~
def getmes():
   #获取主表数据，生成id
   getdetail(id)
   
   
   
def getdetil(id):
   #查询详情表
   detail = Detail.objects.all()
   host="http://w33243.com/detail/"
   for i in deatil:
       url = host+i.id
       try:
         res = request.get(url,headers={"":""})
         tt = json.loads(res.text)
       except:
          redis.lpush('asdf',i)
 
 def detail():
    id = redis.rpop('asdf')
  
  	res = request.get(url,headers={"":""})
  	tt = json.loads(res.text)
     
~~~



角色的资源配制

资源互斥

~~~
互斥表
res1  res2
 1      2
 3      1
 5      6
 
 
角色配制资源
1，3，5
#查询此角色继承的资源 24
#合并资源 list= 2，3，5
#查询互斥表
for i in list:
    res = mutext.objects.filter(res1=i).first()
    if res.res2 in list:
       return ‘存在互斥不能配制’



 select res.*,pres.name as pname from roles_resources as rr inner join resource as res on rr.resource_id=res.id  inner join resource as pres on res.pid=pres.id where rr.roles_id=1;
 
 
 
 
 用户表
 id  name password roleid
 
 角色表
 id  name
 
 资源表
 id  name pid
 
 角色资源表
 roleid  resid
 
users =  AdminUser.objects.filter().first()

if users:
   #查询此用户对应的角色
   roleid = users.roleid
   #查询角色所对应的资源
   
   select res.id,res.name,pres.id as pid, pres.name as pname from roles_resources as rr inner join resource as res on rr.resource_id=res.id inner join resource as pres on res.pid=pres.id where rr.roles_id=1;
 
 

~~~

![image-20230828085749110](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20230828085749110.png)

### 二进制位运算

~~~
用户表
角色表
id name  pomition
1  管理员   10

资源表
id name       pid    pomistion
1  用户管理     0       
2   用户列表    1         1
3   角色管理    1         2
4   资源管理    1         4

5  视频管理     0      
6  长视频       5         8

| 配制权限
& 获取权限
^ 删除权限


select res.id,res.name,pres.id as pid,pres.name as pname from resource as res inner join resource as pres on res.pid=pres.id where res.pid>0;

~~~

