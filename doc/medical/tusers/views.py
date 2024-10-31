from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

from tools.sflogin import ProductFactory
#获取钉钉url
class DingdingUrl(APIView):
    def get(self,request):
        types = request.GET.get('types')
        p = ProductFactory()
        dclass = p.create_product(types)
         
        # redirect_uri = "http://127.0.0.1:8000/user/dingtalkCallback/"
        # client_id = "dingqxjco4n5jjtt7ctj"
        # url = "https://login.dingtalk.com/oauth2/auth?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=dddd&prompt=consent"%(redirect_uri,client_id)
        return Response({"code":200,'url':dclass.geturl()})
        
import requests
#钉钉回调接口
class DingdingCallback(APIView):
    def get(self,request):
        authCode = request.query_params.get('code')

        # 根据authCode获取用户accessToken
        data = {
            "clientId": "dingqxjco4n5jjtt7ctj",
            "clientSecret": "cQJnGlcoMmz6Nnv-r0aFEpQAHqiwVK0t4yf1J_9Do8jQP1AV81iVT2M3GXHWLy53",
            "code": authCode,
            "grantType": "authorization_code"
        }
        resp = requests.post('https://api.dingtalk.com/v1.0/oauth2/userAccessToken', json=data).json()
        accessToken = resp.get('accessToken')

        # 根据accessToken获取用户信息
        headers = {"x-acs-dingtalk-access-token": accessToken}
        resp = requests.get('https://api.dingtalk.com/v1.0/contact/users/me', headers=headers).json()
        name = resp.get('nick')
        uid = resp.get('openId')
        phone = resp.get('mobile')
        print(resp)
        return Response({"code":200})
    
from qiniu import Auth
class QnToken(APIView):
    def get(self,request):
         #需要填写你的 Access Key 和 Secret Key
        access_key = '10XJP3-oMzY2Ghrwsm6nc-fr1OKu_-HcRwweQ1AB'
        secret_key = 'L3yUOFzGq3zJwqy924JPvMg61H88COZZ8feUcAJj'
        #构建鉴权对象
        q = Auth(access_key, secret_key)
        #要上传的空间
        bucket_name = 'h2402a'

        #3600为token过期时间，秒为单位。3600等于一小时
        token = q.upload_token(bucket_name)
        return Response({"code":10000,'data':token})
from tools.bdapi import bdapi
from tools.myredis import r
class Idcard(APIView):
    def get(self,request):
        #获取图片url
        url = request.GET.get('picurl')
        #调用百度api处理
        r.list_push('baiduurllist',url)
        # mes = bdapi.fontmessage(url)
        #返回数据
        return Response({"code":200})
    
    def post(self,request):
        blist = r.list_lrange('baiduurllist',0,10)
        if blist:
            for i in blist:
                picurl = i.decode()
                mes = bdapi.fontmessage(picurl)
                print(mes)
                #存入redis
                r.set_str(picurl,json.dumps(mes))
                r.list_del('baiduurllist',picurl)
        
        return Response({"code":200})
import json
class BaiduUsermes(APIView):
    def get(self,request):
        url = request.GET.get('picurl')
        mes = r.get_str(url)
        code = 10010
        if mes:
            mes = json.loads(mes)
            code = 200
            r.str_del(url)
        return Response({"code":code,'mes':mes})
    
    
def read_large_file(file_path):  
    """  
    使用生成器逐行读取大文件  
    :param file_path: 文件的路径  
    :return: 生成器，每次迭代产生文件的一行  
    """  
    with open(file_path, 'r', encoding='utf-8') as file:  # 假设文件是utf-8编码  
        for line in file:  
            yield line.strip()  # 移除行尾的换行符，并返回该行

#    large_file_path = 'path/to/your/large/file.txt'  
#     for line in read_large_file(large_file_path):  
#         print(line)  # 处理每一行  
#         # 这里可以根据需要对每行数据进行处理，例如写入数据库、进行数据分析等  
#         # 因为使用了生成器，所以无论文件多大，内存使用都会保持在一个较低的水平
                
from elasticsearch import Elasticsearch
# 创建es 实例39.105.220.219
es = Elasticsearch("http://47.95.14.195:9200/")

class DockerSearch(APIView):
    def post(self,reqeust):
        #查询医生表，id   name   描述
        #查询健康知识表  id  title 描述
        # docker = Docker.objects.all()
        # es.indices.delete(index='doctor')
        print(es)
        for row in range(10):
            print(row)
            # index就是对应的一张表 eg.对应的就是course表
            es.index(index='doctor', body={
                'id': row,
                'table_name': 'doctor',
                'name': "张三"+str(row),
                'descrip': "asfsdfsd描述"+str(row),
            })
                
            
        return Response({"code":200})
    def get(self,request):
        page = request.GET.get('page')
        pagesize = 2
        start = (int(page)-1)*pagesize
        keyword = request.GET.get('sname')
        
        dsl={
            "query":{
                "match":{"name":keyword}
            },
            "from":start,
            "size":pagesize
        }
        
        res = es.search(index="doctor", body=dsl)
        data = res['hits']['hits']
       
        rlist = []
        for i in data:
            rlist.append(i['_source'])
        
        
        dsl={
            "query":{
                "match":{"name":keyword}
            }
        }
        total = es.count(index="doctor", body=dsl)
        return Response({"code":200,'rlist':rlist,"total":total['count']})

from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
from langchain_core.output_parsers import CommaSeparatedListOutputParser,NumberedListOutputParser

class MessageView(APIView):
    def get(self,request):
    
        #用户经常查看的文章
        # l1 = list(ArticleView.objects.filter(user_id=1).values("id","title"))
        l1 = [{"id":1,'mes':'时尚'},{"id":2,'mes':'商务'}]
        
        #从文章表中查询近两个月的数据获取 id  摘要
        #假设已经有这么多的提示词示例组：
        examples =  [  
            {"id": "1", "features": "心长病突然哪天是"},  
            {"id": "2", "features": ', '.join(["休闲", "运动鞋", "篮球"])}, 
            {"id": "3", "features": ', '.join(["商务", "皮鞋", "正装"])}, 
            {"id": "4", "features": ', '.join(["户外", "徒步鞋", "探险"])}, 
            {"id": "5", "features": ', '.join(["时尚", "板鞋", "滑板"])}, 
        ]  

        #构造提示词模板
        example_prompt = PromptTemplate(
            input_variables=["id","features"],
            template="找出id:{id}\n描述：{features}",
        )

        #调用MMR
        example_selector = SemanticSimilarityExampleSelector.from_examples(
            #传入示例组
            examples,
            #使用阿里云的dashscope的嵌入来做相似性搜索
            DashScopeEmbeddings(),
            #设置使用的向量数据库是什么
            FAISS,
            #结果条数
            k=3,
        )

        #使用小样本提示词模版来实现动态示例的调用
        dynamic_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix="查询和features相似度最高的id",
            suffix="关键词为：{word}",
            input_variables=["word"]
        )
        str = ''
        for i in l1:
            str +=i['mes']
            
        
        # print(dynamic_prompt.format(word=str))
        qq = dynamic_prompt.format(word=str)
        print(qq)
        return Response({"code":200})
    

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
   
class TestWebsocket(APIView):
    def get(self,request):
        number = request.GET.get('count')
        send_data=[{"name":"内科","count":number},{"name":"外科","count":130}]
        
        channel_layer = get_channel_layer()
      
        async_to_sync(channel_layer.group_send)(
            '1001',#房间组名
            {
                'type':'send_to_chrome', #消费者中处理的函数
                'data':send_data
            }
        )
        return JsonResponse({"code":200,"msg":"更新数据成功"})
from .ser import *
import time
class DeptManager(APIView):
    def get(self,request):
        #获取科的信息
        #加缓存优化，并发访问
        deptlist = r.get_str('deptlist')
        if deptlist:
            deptlist = json.loads(deptlist)
            return Response({"code":200,'data':deptlist})
        #并发访问
        
        if r.setnx_str('deptflag',"1"):
            dept = DepartMent.objects.filter(pid__isnull=True).all()
            ser = DeptSer(dept,many=True)
            r.set_str('deptlist',json.dumps(ser.data))
            r.str_del('deptflag')
            return Response({"code":200,'data':ser.data})
        else:
            time.sleep(2)
            deptlist = r.get_str('deptlist')
            if deptlist:
                deptlist = json.loads(deptlist)
                return Response({"code":200,'data':deptlist})
            else:
                return Response({"code":10010,'message':"请刷新页面。。。"})
# 1导入prompt的类
from langchain.prompts import PromptTemplate
# 导入通义大模型
from langchain_community.llms import Tongyi   
from langchain.prompts import ChatMessagePromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
      
class AricleComment(APIView):
    def post(self,request):
        data = request.data
        userid = 1
        articleid = 1
        comment = "这个关于医疗的文章不错，里面有关于高血压的介绍"
        # comment = "这个关于医疗的文章写的不好，里面有关于高血压的介绍"
       
        # # 定义一个模板
        # pp = "你是一个评价师，请根据输入内容，判断分类 1为好评 2为中评 3为差评，输入内容为{mes},输出为123"
         # 实例化模板类
        # promptTemplate = PromptTemplate.from_template(pp)
        # prompt = promptTemplate.format(mes=comment)
        
        # 定义列表解析器
        output_parser = CommaSeparatedListOutputParser()
        format_instructions = output_parser.get_format_instructions()
        
        message = "请根据输入内容，判断分类 1为好评 2为中评 3为差评，输入内容为{mes},输出为123.\n{format_instructions}"
        # 实例化
        promptTemplate = ChatMessagePromptTemplate.from_template(role = "一个评价正常准确的专科医生",template=message,
        input_variables=["mes"],partial_variables={"format_instructions": format_instructions},)

        prompt = promptTemplate.format(mes=comment)
       
        # 实例化通义大模型
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt.content)
        print(ret)
        return Response({"code":200,'mes':ret})
    
    
class Patients(APIView):
    def get(self,request):
        id = request.GET.get('id')
        if id:
            #根据id查询患者
            dict = {"id":1,'name':'张三','defaultFlag':1}
            return Response({"code":200,"data":dict})
        userid = request.GET.get('userid')
        list = [{"id":1,'name':'张三','defaultFlag':1},{"id":2,'name':'李四','defaultFlag':0}]
        return Response({"code":200,"data":list})
    

class Preorder(APIView):
    def get(self,request):
        #获取问诊及医生类型，userid
        #查询价格表
        #查询可用积分去用户表中
        #去优惠券表中查询可用的优惠券
    
        return Response({"code":200,"data":{"pointDeduction":100,'couponDeduction':10,'couponId':1,'payment':100,'actualPayment':80}})
    
import uuid 
class Orderskey(APIView):
    def get(self,request):
        token = uuid.uuid1().hex
        r.setex_str(token,60,token)
        return Response({"code":200,'data':token})
    
import datetime,random
class OrdersView(APIView):
    def post(self,request):
        # 1.获取数据
        data = request.data
        # 2.接口幂等性判断
        orderkey = data['orderkey']
        value = r.get_str(orderkey)
        userid = 1
        value='222'
        if value:
            # 3.根据orderkey查询redis,如果不存在返回不能生成
            # 4.如果存在生成订单，删除redis中的orderkey
            count = r.get_str('storecount')
            count=10
            if int(count)>=1:
                #写入订单表，更新用户表的锁定积分字段，更新我的优惠券表的中状态为已使用
                #获取费用
                fee = Fee.objects.filter(types=data['type'],docker_types=data['illnessType']).first()
                tmoney = fee.money
                #查询优惠券
                usercoupon = UserCoupon.objects.filter(id=data['couponId']).first()
                couponmoney=0 
                if usercoupon:
                    couponmoney = usercoupon.money
                    
                #积分
                users = Tusers.objects.filter(id=userid).first()
                score = users.tscore
                #总钱数-优惠券
                acmoney = tmoney - couponmoney
                #使用积分数量
                userscore = min(acmoney,score)
                #积分优惠
                pay_money = acmoney-userscore
                    
                orderno =  datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S")+str(userid)+str(random.randint(10000,99999))
                orderdict = {"orderno":orderno,"descrip":data['illnessDesc'],'times':data['illnessTime'],'pic_url':json.dumps(data['pictures']),
                             "is_into":data['consultFlag'],'patient':data['patientId'],'userid':userid,'status':1,'transaction':'0',
                             "pay_type":1,'docker_types':data['illnessType'],'types':data['type'],'department':data['depId'],
                             "score":userscore,'couponid':data['couponId'],'couponmoney':couponmoney,'tmoney':tmoney,'pay_money':pay_money}
                ser = OrdersSer(data=orderdict)
                if ser.is_valid():
                    ser.save()
                    #更新锁定积分
                    users.lock_score +=userscore
                    users.save()
                    #更新优惠券表
                    if usercoupon:
                        usercoupon.is_used=True
                        usercoupon.save()
                    #更新号源redis的分步式锁
                    r.decr_str('storecount',1)
                    #删除幂等性操作
                    r.str_del(orderkey)
                    #生成订单加入队列，半小时没支付订单处理
                    r.zset_zadd('ordercancle',int(time.time()),orderno)
                    return Response({'code':200,'orderno':orderno})
                else:
                    print(ser.errors)
                    return Response({"code":10011,'mes':ser.errors})
            else:
                return Response({"code":10010,'mes':'号源不足'})
            # 5.判断库存，生成订单，锁定积分（用户表中加一个锁定积分字段）、锁定优惠券（已经使用）
        else:
            return Response({"code":10010,'mes':'已经生成过不能重复'})
from tools.comm import get_alipay
class Pay(APIView):
    def post(self,request):
        data = request.data
        orderId = data['orderId']
        #查询订单
        pay = get_alipay()
        orderno = random.randint(1000,9999)
        pay_money=100
        query_params = pay.direct_pay(
                subject="问诊支付",  # 商品简单描述
                out_trade_no=str(orderno),  # 用户购买的商品订单号（每次不一样） 20180301073422891
                total_amount=float(pay_money),  # 交易金额(单位: 元 保留俩位小数)
            )
        payUrl = "https://openapi-sandbox.dl.alipaydev.com/gateway.do?{0}".format(query_params)
      
        return Response({"code":200,'url':payUrl})
    
class Alipaycallback(APIView):
    def get(self,request):
        data = request.GET
        mes = {k:v for k,v in data.items()}
        #验证签名
        pay = get_alipay()
        sign = mes.pop('sign')
        flag = pay.verify(mes,sign)
        if flag:
            print("####")
            print(data)
            orderno = data['out_trade_no']
            #将支付过的订单删除
            r.zset_zrem('ordercancle',orderno)
            #加入成功队列表中，后续异步分配及操作
            r.list_push('ordersuccess',orderno)
            #通过不通过重定向到vue页面，提示订单不存在
            #如果通过从data中获取订单号和支付宝流水号
            #根据订单号更新订单表
            #判断支付状态，如果成功，订单号写入队列
            # return HttpResponseRedirect("http://localhost:80/success")
        return Response({"code":200})
            
        
        
        #更新用户表积分，锁定积分-，总积分-
        #写入积分记录表
        #分配医生同步异步
        
        
import os
from medical import settings
db=None
# 导入所需的模块和类
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.dashscope import DashScopeEmbeddings

from langchain_text_splitters import CharacterTextSplitter

def generate_sse(chunks):
    for chunk in chunks:
        data = f"data: {chunk}\n\n"
        if chunk:
            yield data.encode('utf-8')
        else:
            print('____________')
            return 'no mes'
        
            
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET           

@require_GET
def sse_notifications(request):
        query_text = request.GET.get('ask')  # 调用函数获取用户输入 
    
        # 实例化模板类
        pp = "帮我优化一下{res}中信息"
       
        promptTemplate = PromptTemplate.from_template(pp)
        prompt = promptTemplate.format(res=query_text)
         
            
        llm=Tongyi(
            model="qwen-turbo",
            temperature=0,
            max_tokens=512,
        )
   
        chuns = llm.stream(prompt)
                   
        response = StreamingHttpResponse(
            generate_sse(chuns),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        return response


class FileUpload(APIView):
    def post(self,request):
        file = request.FILES['file']
        # 生成文件路径  
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)  
        with open(file_path, 'wb+') as destination:  
            for chunk in file.chunks():  
                destination.write(chunk) 
        #读取写入向量数据库  
        global db
        # 实例化向量嵌入器
        embeddings = DashScopeEmbeddings()
        # 初始化缓存存储器
        store = LocalFileStore("./cache/")
        # 创建缓存支持的嵌入器
        cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
        
        # 加载文档并将其拆分成片段
        doc = TextLoader(file_path,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=500, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
        # 创建向量存储
        db = FAISS.from_documents(chunks, cached_embedder) 
        return Response({"code":200})   
    
    def get(self,request):
        #获取问题
        query_text = request.GET.get('ask')
        #判断问题是否存在
        if query_text: 
            #更义直接查询大模型
            res = None
            pp = "根据{res}返回结果"
            #判断向量数据库是否，如果存在从向量数据库中查
            if db:
                #查询的信息是否存在 
                res = db.similarity_search("NBA冠军球队是哪个", k=3)
               
                if res:
                    #向量数据库中有值构造prompt
                    pp = "帮我优化一下{res}中信息"
            #调用通义千问查询
            
            # 实例化模板类
            promptTemplate = PromptTemplate.from_template(pp)
            # 生成prompt
            if res:
                prompt = promptTemplate.format(res=res)
                print('faiss:',prompt)
            else:
                prompt = promptTemplate.format(res=query_text)
                
            tongyi = Tongyi()
            ret = tongyi.invoke(prompt)
            print(ret)
            return Response({"code":200,'mes':ret})
        else:
            return Response({"code":10010,'mes':'请输入你的问题'})

from langchain_community.llms import Tongyi
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()

class TestDoctor(APIView):
    # def get(self,request):
    #     doctorid =1
    #     name = request.GET.get('name')
    #     id = request.GET.get('id')
    #     #发送推送消息
    #     channel_layer = get_channel_layer()
    #     message = {"name":name,'id':id}
    #     async_to_sync(channel_layer.group_send)(
    #         "doctor"+str(doctorid),#房间组名
    #         {
    #             'type':'send_to_chrome', #消费者中处理的函数
    #             'data':message
    #         }
    #     )
    def get(self,request):
        #获取用户输入
        ask = request.GET.get('ask')
        #查询向量数据库
        #输入信息加入memory
        #查询redis构造memory
        memory.chat_memory.add_user_message(ask)
        #调用模型查询答案
        #答案加入memory
        #返回结果
        llm = Tongyi(temperature=0)
        #加一个prompt  "我的问题{ask},请从以下文章中获取答案{res}"
        conversation = ConversationChain(
            llm=llm, 
            # verbose=True, 
            memory=memory
        )
        res = conversation.predict(input=ask)
        print(res)
        memory.chat_memory.add_ai_message(res)
        memory.load_memory_variables({})
        return Response({"code":200,'mes':res})
        
from tools.db import db
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.reduce import ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate
from langchain.chains.sequential import SequentialChain

class TestDemo(APIView):
    def post(self,request):
        # res = requests.get('http://asfsdf.com/')
        # content = json.loads(res.text)
        # # 加载文档并将其拆分成片段
        # # doc = TextLoader("./doc/1.txt",encoding='utf-8').load()
        # spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        # chunks = spliter.split_documents(content)
        # db.add(chunks)
        
        # #英文的Pdf
        # llm = Tongyi()
        # #load pdf
        # loader = PyPDFLoader("doc/demo.pdf")
        

        llm = Tongyi()

        

        #chain 1 任务：翻译成中文
        first_prompt = ChatPromptTemplate.from_template("把下面内容翻译成中文:\n\n{content}")
        chain_one = LLMChain(
            llm=llm,
            prompt=first_prompt,
            # verbose=True,
            output_key="Chinese_Rview",
        )

        #chain 2 任务：对翻译后的中文进行总结摘要 input_key是上一个chain的output_key
        second_prompt = ChatPromptTemplate.from_template("用一句话总结下面内容:\n\n{Chinese_Rview}")
        chain_two = LLMChain(
            llm=llm,
            prompt=second_prompt,
            # verbose=True,
            output_key="Chinese_Summary",
        )

        #chain 3 任务:智能识别语言 input_key是上一个chain的output_key
        third_prompt = ChatPromptTemplate.from_template("根据下面内容写5条评价信息:\n\n{Chinese_Summary}")
        chain_three = LLMChain(
            llm=llm,
            prompt=third_prompt,
            # verbose=True,
            output_key="Language",
        )

        #chain 4 任务:针对摘要使用指定语言进行评论 input_key是上一个chain的output_key   
        fourth_prompt = ChatPromptTemplate.from_template("请使用指定的语言对以下内容进行回复:\n\n内容:{Chinese_Summary}\n\n语言:{Language}")
        chain_four = LLMChain(
            llm=llm,
            prompt=fourth_prompt,
            # verbose=True,
            output_key="Reply",
        )

        #overall 任务：翻译成中文->对翻译后的中文进行总结摘要->智能识别语言->针对摘要使用指定语言进行评论
        overall_chain = SequentialChain(
            chains=[chain_one, chain_two, chain_three, chain_four],
            # verbose=True,
            input_variables=["content"],
            output_variables=["Chinese_Rview", "Chinese_Summary", "Language"],
        )

        doc = TextLoader("/Users/hanxiaobai/Downloads/dxb/h2402a/medical/tools/doc/1.txt",encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
        
        # content = "I am a student of Cumulus Education, my course is artificial intelligence, I like this course, because I can get a high salary after graduation"
        ret = overall_chain.invoke(chunks)
        print(ret)
        db.add(ret)
        return Response({"code":ret})
    def get(self,request):
        ask = request.GET.get('ask')
        room = request.GET.get('room')
        #查询向量数据库
        contents = db.search(ask)
        prompt = "请帮我从{content}中找出与问题{ask}最相近的答案"
        # 实例化模板类
        promptTemplate = PromptTemplate.from_template(prompt)
        prompt = promptTemplate.format(content=contents,ask=ask)
     
        memory.chat_memory.add_user_message(ask)
        #调用模型查询答案
        #答案加入memory
        #返回结果
        llm = Tongyi(temperature=0)
        #加一个prompt  "我的问题{ask},请从以下文章中获取答案{res}"
        conversation = ConversationChain(
            llm=llm, 
            # verbose=True, 
            memory=memory,
            prompt=prompt
        )
        res = conversation.predict(content=contents,ask=ask)
        memory.chat_memory.add_ai_message(res)
        memory.load_memory_variables({})
        
        channel_layer = get_channel_layer()
      
        async_to_sync(channel_layer.group_send)(
            room,#房间组名
            {
                'type':'send_to_chrome', #消费者中处理的函数
                'data':res
            }
        )
        

import snowflake.client
def getsnowcode():
    #新生成的id
    code = snowflake.client.get_guid()
    #查询redis
    ocode = r.get_str('snowid')
    if ocode:
        ocode = ocode.decode()
        if int(ocode)>=code:
            return getsnowcode()
    r.set_str('snowid',code)
    return code
        
class PublishView(APIView):
    def post(self,request):
        pass
    #     #接收参数
    #     userid = 1
    #     #调用大模型生成摘要
    #     #写入表，用雪花算法生成唯一id
    #     id = getsnowcode()
    #     #写入哪张表
    #     number = hash(userid)%3
    #     if number == 0:
    #         Publish0.objects.create()
    #     elif number == 1:
    #         Publish1.objects.create()
    #     else:
    #         Publish2.objects.create()
        
    # def get(self,request):
    #     userid = 1
    #     number = hash(userid)%3
    #     if number == 0:
    #         Publish0.objects.filter(userid=userid)
    #     elif number == 1:
    #         Publish1.objects.create()
    #     else:
    #         Publish2.objects.create()
            

import pymongo
from urllib import parse
username = parse.quote_plus('admin')   # 对用户名进行编码
password = parse.quote_plus('123456')  # 对密码进行编码
database = "admin" # 数据库名称
host= "47.95.14.195"
port= "27017"
mongo = pymongo.MongoClient('mongodb://%s:%s@%s:%s/%s' % ( username, password, host, port, database))
my_db = mongo["my_db"]



def generate_tree(source, parent):
     tree = []     
     for item in source:
         if item["parent"] == parent:
             item["child"] = generate_tree(source, item["id"])
             tree.append(item)
     return tree 
       
        
class TestMongo(APIView):
    def post(self,request):
        userid = 1
        newsid = request.data['newsid']
        title = request.data['title']
        content = request.data['content']
        pid = request.data['pid']
        
        my_collection = my_db["news_comment"]
        
        # 添加一个文档
        document = { "userid": userid, "newsid": newsid,"title":title,"content":content,"pid":pid}
        ret = my_collection.insert_one(document)
        return Response({"code":200})
    
    def get(self,request):
        # query = { "newsid": '1' }
        # my_collection = my_db["news_comment"]
        # document_list = my_collection.find(query)
        # lists=[]
        # for document in document_list:
        #     lists.append({"id":document['_id'],'title':document['title'],'pid':document['pid']})
        
        permission_source = [{"id": 1, "name": '电器', "parent": 0},
         {"id": 2, "name": '水果', "parent": 0},
         {"id": 3, "name": '家用电器', "parent": 1},
         {"id": 13, "name": '1111家用电器', "parent": 3},
         {"id": 4, "name": '电吹风', "parent": 2},
         {"id": 5, "name": '电风扇', "parent": 3},
         {"id": 6, "name": '台灯', "parent": 3},
         {"id": 7, "name": '商用电器', "parent": 1},
         {"id": 8, "name": '大型电热锅', "parent": 7}]
        permission_tree = generate_tree(permission_source, 0)
        print(json.dumps(permission_tree, ensure_ascii=False)) 
        return Response({"code":200,'list':permission_tree})
        
        
        
import os   
import shutil
 
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(fp)
                total_size += size
            except OSError:
                pass  # Ignore files that can't be accessed
    return total_size
import uuid
#文件上传
def fileupload(request):
    #获取参数
    data = request.POST
    img = request.FILES.get('file')
    filename = data['filename']
    tcount = int(data['tcount'])
    count = int(data['count'])
    size = int(data['size'])
    fname = uuid.uuid1().hex
    #上传代码 os.rename() uuid.uuid().hex
    arr = filename.split('.')
    filepath = f'./static/upload/{filename}'
    if not os.path.exists(filepath):
        os.mkdir(f'./static/upload/{filename}')
    
    with open(f'./static/upload/{filename}/{count}', 'wb') as f:
        for chunk in img.chunks():
            f.write(chunk)
            # f.close()
    fsize = get_folder_size(filepath)
    if size == fsize:
        #合并
        with open(f'./static/upload/{fname}.{arr[1]}', 'wb') as f:
            for i in range(tcount):
                with open(f'./static/upload/{filename}/{i}', 'rb') as chunk:
                    f.write(chunk.read())
        #删除文件夹
        # if os.path.exists(filepath):
        #     shutil.rmtree(filepath)
         #os.remove(f'./static/upload/{filename}/{i}')
        return JsonResponse({"code":200})
    else:
         return JsonResponse({"code":10010})