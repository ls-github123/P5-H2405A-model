### 1.三方登录

~~~
1.微博平台配制
2.在登录页面加一个图标，调用接口获取微博url
3.

表设计
用户表
id  mobile username   
1  2423423   张三
2  23324234  李四


qq  weibo  weixin  dingding

三方登录表
id  userid  webfrom   uid        token
1     1      qq        234234    asfasfsfsdf
2     1      weibo     abcas32423   afwrwresdfdf




~~~

### 2.百度qps限制

~~~
个人2qps
企业10qps
每秒实证认证的人是10个
队列
图片的url,将url放入队列
定时任务每秒执行一次：从队列中取出2条数据，调用百度接口，返回数据放到redis,key 图片url value:{"name":'34','code':'234'}

vue setInteval每秒请求一个接口：携带图片地址这个参数，通过这个参数去redis中查询，如果有数据直接返回，clearInterval

websocket

百度企业10qps，20qps
队列：
1.图片上传到云服务器，调用接口，将图片地址写入队列中
2.定时任务django-celery每隔一秒执行一次，从获取中获取10条，发送请求，获取到结果，把结果存在redis
3.setInterval每隔一秒去获取信息，拿到数据clearInterval
~~~

~~~
半小时内没支付订单的处理

Mysql
redis
1.生成订单的时候订单号存入队列
2.在支付成功的回调接口中删除已经支付的订单号
3.此时队列中的数据没支付的，定时任务对半小时没支付订单处理

定时任务

任务体
def task():
    #查询队列中半小时前的订单号
    #如果存在从mysql订单表移除到取消订单表
    #恢复商品表中锁定库存
    #删除队列中的订单号
    
~~~

定时任务

~~~
linux crontab
常用的定时任务框架 celery  aps

interval  每秒执行，每小时执行
date   指定日期  2023-12-05 8:00
cron  灵活，都能支持
~~~

### 2.celery使用

~~~
celery异步任务框架，没有内置队列，需要引入redis或者是rabbitmq做为队列
1.task任务
2.beat定时任务
3.broker中间人，监听任务，拿到任务，把任务放到quque中
4.worker消费者，做任务的
5.backend存放任务结果



~~~



1.安装

~~~
celery是一个异步任务框架，没有队列。redis,rabbitmq

task  产生任务     
beat  定时任务配制
broker  任务调用器，将任务放入队列
worker  监听队列变化，执行任务
backend  将任务结果存入到结果队列中
~~~

<img src="images/26.png">



~~~
pip uninstall celery
pip intall -U celery
~~~

2.在settings中配制

~~~python
# Celery配置
# from kombu import Exchange, Queue
# 设置任务接受的类型，默认是{'json'}
CELERY_ACCEPT_CONTENT = ['application/json']
# 设置task任务序列列化为json
CELERY_TASK_SERIALIZER = 'json'
# 请任务接受后存储时的类型
CELERY_RESULT_SERIALIZER = 'json'
# 时间格式化为中国时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 是否使用UTC时间
CELERY_ENABLE_UTC = False
# 指定borker为redis 如果指定rabbitmq CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# 指定存储结果的地方，支持使用rpc、数据库、redis等等，具体可参考文档 # CELERY_RESULT_BACKEND = 'db+mysql://scott:tiger@localhost/foo' # mysql 作为后端数据库
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
# 设置任务过期时间 默认是一天，为None或0 表示永不过期
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 设置worker并发数，默认是cpu核心数
# CELERYD_CONCURRENCY = 12
# 设置每个worker最大任务数
CELERYD_MAX_TASKS_PER_CHILD = 100


# 指定任务的位置
CELERY_IMPORTS = (
    'base.tasks',
)
# 使用beat启动Celery定时任务
# schedule时间的具体设定参考：https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'base.tasks.cheduler_task',
        'schedule': 10,
        'args': ('hello', )
    },
}

~~~

在settings同级目录下新celery.py

~~~python
# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mall.settings')
app = Celery('mall',broker='redis://127.0.0.1:6379/1',  # 任务存放的地方 
             backend='redis://127.0.0.1:6379/15')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

platforms.C_FORCE_ROOT = True


~~~

在settings同级目录__init__.py中

~~~python
# from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

~~~

在项目目录下创建base文件夹，在base下新建tasks.py文件

~~~
# from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task
def cheduler_task(name):
   end = int(time.time())-600
   olist = r.sorted_times(key,0,end)
   for i in olist:
      res = alipay.query_pay(i.decode())
      requests
      content = res.text
      #更新订单更新用户余额

~~~

启动任务

~~~
启动worker
celery -A mall  worker -l info

windows下启动 worker
celery -A mall  worker -l info -P eventlet 
启动定时beat
celery -A mall beat -l info 
~~~





