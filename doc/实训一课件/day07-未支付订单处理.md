1.10分钟内末支付订单的处理

celery写一个定时任务，每一分钟查询数据库中订单表，查询10分钟之前并且没支付的，把订单的状态变为取消5.恢复库存，优惠卷，积分

队列实现

~~~
实现流程
1.生成订单的接口把订单写入数据库，订单号写入到redis中 
2.在支付回调接口中从支付返回的状态判断是否支付成功。更新订单。从redis删除订单号
3.此时队列中数据没支付，celery启动一个定时任务每1分钟执行一次，从redis取出10分钟前的记录

~~~

代码实现

~~~
redis zset sortedset(延时队列)
key score  params

1.订单号和当前时间(int(time.time()))写入到redis中 key='orderlist'
2.从redis删除订单号
3.zrangebyscore('orderlist',0,int(time.time())-600)
~~~

redis封装

~~~
#zset
    def zset_zadd(self,key,score,value):
        map={value:score}
        return self.r.zadd(key,mapping=map)

    def zset_zrem(self,key,value):
        return self.r.zrem(key,value)

    def zset_zrangebyscore(self,key,min,max):
        return self.r.zrangebyscore(key,min,max)
~~~

生成订单的接口中添加

~~~
#生成订单加入队列，半小时没支付订单处理
r.zset_zadd('ordercancle',int(time.time()),orderno)
~~~

在支付回调接口中删除

~~~
#将支付过的订单删除
r.zset_zrem('ordercancle',orderno)
~~~

在定时任务中

~~~
@shared_task
def  cancleorders():
    #从队列中获取信息
    clist = r.zset_zrangebyscore('ordercancle',0,int(time.time())-1800)
    #遍历
    if clist:
        for i in clist:
            orderno = i.decode()
            #更新订单，恢复积分，恢复优惠券,更新库存
            r.zset_zrem('ordercancle',orderno)
~~~

在settings中配制

~~~
CELERYBEAT_SCHEDULE = {
    'getbaidu-1-seconds': {
        'task': 'base.tasks.getbaidu',
        'schedule': 3,
        
    },
    'order_cancle': {
        'task': 'base.tasks.cancleorders',
        'schedule': 60, 
    },
}
~~~

