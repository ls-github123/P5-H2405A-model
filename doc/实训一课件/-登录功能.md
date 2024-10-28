1.加入购物车

~~~
判断是否登录-》如果登录-》查询购物车中是否存在-》存在数量+-》不存在添加

登录流程-》输入用户名、密码（手机号、验证码）、三方登录-》服务端生成jwt token-》返回给客户端-》存入localStorage-》每次请求携带token-》服务端进行验证-》通过继续操作-》不通过返回403


def userinfo():
  pass
  
  
def modify_passwd():
  pass
  
  
  
def getgoodslist():
      pass
  
  

~~~

2. Jwt token

   ~~~
   session   
   客户端向服务端发起请求（携带用户名密码）-》服务端验证成功-》生成一个jsessionid对应一个session文件,session文件中存的是用户信息-》返回存入头部的cookie中-》每次请求携带cookie-》cookie中带jsessionid-》服务端通过jsessionid查询文件-》如果存在取出用户信息-》如果不存在返回没登录
   
   cookie
   客户端，不安全
   
   token
   客户端向服务端发起请求（携带用户名密码）-》服务端验证成功-》生成一个token串，存入mysql或redis中-》返回给客户端-》每次请求携带token-》服务端验证token-》验证通过通过token拿到用户信息-》认证成功继续操作
   
   分步式应用
   192.168.1.1
   192.168.1.2
   
   jwt token
   json web token
   只需要存储在客户端，加密解密实现自认证
   三部分构成：
   头部:指定加密方式{"type":'hash256'}
   载和payload:{data:{"userid":1,'name':'','exp':int(time.time())}}
   签名 hash256(base64(头部).base64(载和),"SECRET_KEY")
   
   生成：
   base64(头部).base64(载和).hash256(base64(头部).base64(载和),"SECRET_KEY")
   
   解析
   asfasdfs234252.asfawr44235246356.
   base64(头部).base64(载和).hash256(base64(头部).base64(载和),"SECRET_KEY")
   用户.分隔获取到签名
   获取前两部分，用前两部分进行hash256加盐生成新的签名，和签名进行对比，如果相同授权通过
   优势：适合分步式应用做单点登录，节约了服务器资源
   ~~~

~~~
jwt话术总结
json web token，用于接口开发中的安全认证。相对于以往的session\cookie\token来说，优势在于实现客户端自认证，服务端不用存储，节约了服务器资源。适于分步式应用下单点登录。session的工作原理客户端向服务端发起请求，服务端进行验证，jsessionid对应一个jsession文件。把jsessionid返回存入cookie，下次请求携带jsessionid.服务端查找jsessionid对应的文件，如果存在取出用户信息，如果不存在显示没有权限操作。分式式应用下有多台服务器，登录负载到A服务器，下单在B服务器就会显示没有权限。当然也可以通过数据存储实现。服务端生成一个token，保存在数据库并且返回给客户端，下次请求携带token,数据库中查询。jwt由三部分构成，头部（加密方式），栽和（携带用户信息和过期时间）和签名。生成base64(头部).base64(栽和).hash256(base64(头部).base64(栽和),'盐'）。解析用.进行分隔，对前两部分用服务器盐进行hash256操作，获取到新的签名和第三部分签名对比，如果相同代表没被修改。

~~~



### 3.注册实现

1.详情页加入购物车判断是否有权限（token）,没有跳转到注册页面

2.在注册页面

![image-20231127103903000](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20231127103903000.png)

输入信息，发起axios post请求

3.写一个注册接口，调用序列化器验证

4.在序列化器中验证validate_name用户名格式8-12位数字加字母

在序列化器中验证validate_mobile验证手机号

​    def validate(self, data):验证两次密码一致

5.保存用户，获取userid

6.封装myjwt

7.用userid,调用myjwt生成token返回

8.vue用localStorage.setItem('token',token)



![image-20231128091010753](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20231128091010753.png)



三方登录流程

微博平台注册应用-》利用信息生成授权url-》点击url进入微博-》授权-》根据微博配制的回调地址进行回调-》在回调接口获取code-》请求access_token接口返回微博用户信息-》查询三方登录表根据uid-》如果存在获取网站的用户信息-》生成token返回-》如果不存在绑定用户-》写入用户表和三方登录表

表设计



### 加入购物车

~~~
1.判断是否登录，如果没登录跳转到登录页面
2.加入购物车，购物车三要素：userid  goodid  count,判断此用户是否购买过此商品
3.我的购物车
~~~

redis

~~~
字符串   
hash 对象 {'user1goods1':{"id":1,'count':5,'is_checked':1},'user1goods2':{"id":2,'count':15,'is_checked':2}}
商品id  count  is_checked
~~~

### redis购物车实现

~~~
购物车
userid  goodid  count   is_checked 

key = 'user1goods1'   id   2
                      count  5
                      is_checked  1
                      good
                      
#获取我的购物车
1.获取userid
2.模糊查询购买了哪些商品
keys = keys("user1goods*")
结果：
user1goods1
user1goods2
user1goods3
3.遍历所有的key,获取所有的商品id
idslist = []
for i in keys:
   goodsid = hget(i,'id')
   idslist.append(goodsid)

goods = Goods.objects.filter(id__in=idslist).all()
gdict = {}
for g in goods:
    gid = int(g.id)
   gdict[gid] = GoodsSer(g) 


reslist=[]
for i in keys:
   goodsid = hget(i,'id')
   count = hget(i,'count')
   
   dict={"id":goodsid,'count':count,'goods':gdict[goodsid]}

                      
                  
                     
~~~

设置默认地址

~~~
传递参数: id ,userid
#Address.objects.filter(userid=1,is_default=True).update(is_default=False)
Address.objects.filter(id=id).update(is_default=True)
~~~

### 生成订单

~~~
判断库存：
查询库存-锁定库存
判断
如果没有库存直接返回不足
如果有直接操作

判断库需要加锁：
悲观锁：直接在数据库上加锁，mysql默认使用的innodb引擎，效率低，精确性高,当事务提交的时候或者回滚的时候释放锁
Goods.objects.select_for_update().filter(id=gid).first()

乐观锁:不在数据库上加锁，先查询库存（记录库存），写入订单表，写入订单详情表，更新锁定库存（判断之前查的和现在的是否一样）如果不一样证明中间已经修改，重新查询
~~~

### 接口幂等性操作

~~~
保证多次提交只产生一次结果，避免网络不好，用户频繁点击导致有问题数据的产生

生成订单
提交表单-》报销

1.在生成订单页面请求接口，接口生成一个全局唯一的key保存并返回
2.客户端保存key,点击生成订单携带key
3.在生成订单的接口中，根据key查询，如果存在删除key,生成订单。如果不存在，不操作直接返回已经生成过，不能频繁操作


~~~

支付流程

~~~
调用获取支付宝链接的接口，参数 订单号
跳转到支付宝，输入密码支付，支付完回调
在回调接口中第一步验签，根据订单号更新订单表，更新库存，库存减购买数据，锁定库存减购买数据，更新销量

http://localhost:8000/users/alipaycallback?charset=utf-8&out_trade_no=1701757716&method=alipay.trade.page.pay.return&total_amount=100.00&sign=CT7ayPgEnH7TjCJqdNh%2FLfXMFUrJxRSw%2BQ0sY5CUCTVHEjl3c9mhcueYLNRARMNos6Npcb%2F8ugCoDGMqHWfmrM%2BQN1I9f0w%2FkQU6GVYogqzBfMOGqUGDJXnrfsMol48p7aeFE1yS%2FHYNZpsZ6Gy%2Fv7c9q8T%2B4y%2FqA0ZdK2tJcEJSKieju7Hmh9fUYYG1nYep05tR%2BXlpFSoAfdJcBRWyK35vEWLKukNtyVcdL8LSVofo1F4rV40pDo7SW8fgYw4OPDrBekKt7YmzhQnCIz2Jr1d1GbOeEKqTsilzeVP4T70V2NbF4oarSY2NYqnaDGr72Mund1i3juIOKhQUCRnWGg%3D%3D&trade_no=2023120522001434530501636072&auth_app_id=9021000132600978&version=1.0&app_id=9021000132600978&sign_type=RSA2&seller_id=2088721021813096&timestamp=2023-12-05+14%3A30%3A28

~~~

