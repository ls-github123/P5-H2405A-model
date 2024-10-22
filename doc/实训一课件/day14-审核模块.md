

### 1.审核模块

~~~
发布视频-》人工审核-》展示

做饭  审核
唱歌
去哪玩

分表中如果读取数据？
多审核员模式？


1.在发布视频接口中将视频code唯一标识加入队列中
myredis.list_add('auditpublish',code)
2.celery定时任务，每分钟执行一次。查询所有审核人，遍历审核，获取队列中的信息分配，更新发布表中的审核人
adminuser = AdminUser.objects.filter(roleid=3).all()
for i in adminuser:
    #审核员id
    id = i.id
    code = myreids.list_pop('auditpublish').decode()
    db_model = Publish(shard_key=code).objects.filter(code = code).first()
    db_model.audit_user = id
    db_model.save()

3.审核员从管理后台登录，-》视频审核-》显示此管理人分配的所有的发布信息
union 和union all
select * from publish0 where audit_user=1 union all select * from publish1 where audit_user=1;

4.审核，通过或者不通过（输入原因）-》写入审核记录表，更新发布表中的审核状态
code  审核状态 status
 db_model = Publish(shard_key=code).objects.filter(code = code).first()
 db_model.audit_status=status
 db_model.save
 AuditPublish(code=code,audit_user=userid,audit_time=date)



~~~



~~~
用户业务端发布视频-》百度敏感词过滤接口（调用添加接口，输入词库）-》人工审核
几十条几百条-》单人审核

发布视频-》写入发布表状态为未审核（1 2通过  3末通过）-》审核员登录后台管理系统-》分页展示所有末审核数据-》详情，

50000 单人不能满足需求，多审核员

审核员的动态分配
id%3
队列  001  002  003  

while True:
     遍历审核员
     for  i in range(3):
         taskid =  r.lpoplpush()
         #更新发布表中的审核员id
         sql = 'update'
     
~~~

2.创建表

~~~
1创建表
2。在角色表中添加一个审核员角色 
3. 给用户配制审核员角色，在资源表中添加视频审核
4.当审核登录成功后显示所有待审核
~~~

### redis事务处理

~~~
Redis 支持事务处理，可以用来保证多个命令的原子性执行。在 Redis 中，事务是通过 MULTI、EXEC、WATCH 和 UNWATCH 四个命令来实现的。

MULTI 命令：用于开启一个事务，将后续的命令添加到事务队列中。

EXEC 命令：用于执行事务队列中的所有命令，如果事务队列中的任何一个命令执行失败，整个事务将被回滚。

WATCH 命令：用于监视一个或多个键，如果在事务执行期间任何一个被监视的键被修改，整个事务将被回滚。

UNWATCH 命令：用于取消对所有键的监视。

以下是一个使用事务处理的例子：

import redis

# 连接 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)

# 定义需要操作的键
key1 = 'key1'  setaudit
key2 = 'key2'  doingaudit

# 开启事务
pipe = r.pipeline(transaction=True)

# 监视 key1 和 key2
pipe.watch(key1, key2)

# 在事务队列中添加命令
pipe.set(key1, 'value1')  
pipe.set(key2, 'value2')  

# 执行事务
try:
    pipe.execute()
except redis.exceptions.WatchError:
    # 如果被监视的键被修改，事务将被回滚
    print('Transaction rolled back')
在这个例子中，我们首先连接 Redis 服务器，并定义了需要操作的键。然后使用 pipeline 方法创建一个 Redis Pipeline 对象，并将 transaction 参数设置为 True，表示开启事务。使用 WATCH 命令监视 key1 和 key2。接着在事务队列中添加了两个 SET 命令，用于设置 key1 和 key2 的值。最后使用 EXEC 命令执行事务。如果在事务执行期间 key1 或 key2 被修改，事务将被回滚，可以在 WatchError 异常中捕获该错误。

需要注意的是，Redis 事务是非常轻量级的，不支持回滚中途的修改。如果事务执行期间发生了错误，整个事务将被回滚，包括事务队列中的所有命令。因此，在使用事务时需要注意避免出现错误，或者在发生错误时手动处理回滚操作。
~~~

### 进程、线程、协程

~~~
进程cpu分配的基本单位，每个进程互相独立，互不影响。适合处理的CPU密集型操作。大量计算处理。进程可以利用cpu多核的特性。
一个进程中包含多个线程，线程之间共享资源。GIL锁，线程受系统调度，线程之间的切换也要占用资源
协程，轻量级线程。用户态，不受系统调用，没有GIL锁，避免了线程切换带来的性能损耗，线程和协程都适合处理IO密集型操作。
多线程内置了GIL，同一时候只有一个线程在执行，为什么程序threading.lock()
GIL相对python解释器在执行程序的时候加的锁
threading.lock()是对业务加锁
~~~

~~~~
1.在发布接口中将code加入队列
2.写一个接口，while True 获取审核员，从队列中取出code，hash取模分配审核员，更新分布表中的审核员id
3.审核员从后台管理系统登录，获取待我审核的信息
select * from (select * from publish0 union all select * from publish1 union all select * from publish2) as publish where audit_user=1  limit 0,10
~~~~

~~~


~~~

### 接口幂等性操作

~~~
多次点击只产生一次结果，发布，生成订单，支付。由于网络慢点击连续发布按钮，数据库增加多条记录。

生成订单页面-》created中调用生成唯一token的接口-》服务端写一个接口，生成一个唯一token（uuid生成），存入redis,返回给客户端-》点击生成订单发送请求携带唯一token-》在生成订单的接口中，从redis中查询如果存在生成订单并且删除redis中的key，如果不存在返回已经生成，不能频繁操作。
~~~



~~~
由于网络慢或者多次点击千万一系列有问题的数据。接口幂等性操作多次同样的点击只产生一次结果。

订单系统为例：
订单接口
def post():
   #获取token串
   token = request.data['token']
   #先去redis中查询，如果存在操作，并且从redis中删除，如果不存在已经操作过不能重复操作
   value = r.str_get(token)
   if value:
     #获取信息
     #生成订单号
     orderno = random.randint(10000,99999)
     #写入订单表
     #删除
     r.str_delete(token)
   else:
      return "不能重复生成订单"

def gettoken():
    code = uuid.uuid1()
    redis.str_add(code,'234')
    return code
在vue页面中moutend中调用接口获取唯一token

在点击提交订单按钮传参，参数是唯一token串
~~~

~~~
select * from (select * from publish0 union all select * from publish1) limit 1,100

标题搜索 添加时间 审核状态
where = '1=1'
if name:
   where = where +" and publis1.name='"+name+"'"
   
if addtime:
		 where = where +" and publis1.addtime="+addtime
		 
		 
"select * from publish1 where "+where

select * from publis1 inner join audit on publis1.code=audit.code  where 1=1  and addtime=


~~~

~~~
mongo    rabbitmq


~~~

