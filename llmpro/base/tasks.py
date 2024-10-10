# from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from tools.mredis import mredis
from tools.bdapi import bdapi
# 1导入prompt的类
from langchain.prompts import PromptTemplate
# 导入通义大模型
from langchain_community.llms import Tongyi

@shared_task
def getbaidu():
   print("调用百度api接口")
   #每秒执行一次从队列中读取5条数据处理，调用百度接口，根据结果做业务操作，更新表的状态
   ids = mredis.list_lrange('dblist',0,4)
   for i in ids:
       print(i)
       code = i.decode()
       publish = Publish.objects.filter(id=code).first()
       res = bdapi.audit_mes(publish.content)
       if res == '1':
           Publish.objects.filter(id=code).update(status=3)
       else:
            # 定义一个模板
            pp = "对文章{mes}进行优化处理"
            # 实例化模板类
            promptTemplate = PromptTemplate.from_template(pp)
            # 生成prompt
            prompt = promptTemplate.format(mes=publish.content)

            # 实例化通义大模型
            tongyi = Tongyi()
            ret = tongyi.invoke(prompt)
            Publish.objects.filter(id=code).update(status=2,content=ret)
        mredis.list_lrem('dblist',code)
       
       

