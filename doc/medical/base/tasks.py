# from __future__ import absolute_import, unicode_literals
from celery import shared_task
import json,time
from tools.myredis import r
from tools.bdapi import bdapi
from tusers.models import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@shared_task
def getbaidu():
    blist = r.list_lrange('baiduurllist',0,10)
    if blist:
        for i in blist:
            picurl = i.decode()
            mes = bdapi.fontmessage(picurl)
            #存入redis
            r.set_str(picurl,json.dumps(mes))
            r.list_del('baiduurllist',picurl)
            
    print("调用百度api接口")
    
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
            
@shared_task         
def successorder():
    #获取队列的长度，如果大于0
    len = r.list_len('ordersuccess')
    if len>0:
        orderno = r.list_pop('ordersuccess')
        orders = Orders.objects.filter(orderno=orderno).first()
        # 分配医生
        # 1.获取订单号orderno = r.rpop()
        # 2.查询订单表
        # 4.根据订单中积分字段，更新积分写入积分记录表
        users = Tusers.objects.filter(id=orders.userid_id).first()
        if orders.score>0:
            users.lock_score -=orders.score
            users.tscore -=orders.score
            users.save()
            Score.objects.create(userid=orders.userid_id,l_type=2,score=orders.score)
        # 5.根据订单对应的科室，查询些科室下的医生
        doctorlist = Doctor.objects.filter(deptid_id=orders.department_id).all()
        # 6.把医生id放入列表中 dlist = []
        dlist = [i.id for i in doctorlist]
        # 7.分配  index = hash(订单号)%len(dlist) 获取到下标  doctorid= dlist[index]
        index = hash(orderno)%len(dlist)
        doctorid = dlist[index]
        # 8.写入医生患者表AssociatedDoctor
        PatientDoctor.objects.create(userid=orders.userid_id,doctorid=doctorid,patient=orders.patient_id,
                                     status=1,orderno=orderno)
        
        #发送推送消息
        channel_layer = get_channel_layer()
        message = {"name":users.name,'id':users.id}
        #根据医生id查询医生表，登录状态1登录  2没登录
        doctor = Doctor.objects.filter(id=doctorid).first()
        if doctor.status == 1:
            async_to_sync(channel_layer.group_send)(
                "doctor"+str(doctorid),#房间组名
                {
                    'type':'send_to_chrome', #消费者中处理的函数
                    'data':message
                }
            )
        
        #key     key value
        #  doctor1user1  name  zs   id   1
        #  doctor1user2  name lishi  id  2
        #  doctor1*
        # r.hash_add()

    
   

