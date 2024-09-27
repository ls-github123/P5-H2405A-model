from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from tools.textload import getdoc
import os
# Create your views here.
from tools.faissdb import faissdb

class Test(APIView):
    def get(self,request):
        
        from bs4 import BeautifulSoup
        res = requests.get('https://movie.douban.com/',headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        movies = []

        for review in soup.find_all('div', class_='review'):
            movie_link_tag = review.find('div', class_='review-hd').find('a')
            movie_title_tag = review.find('div', class_='review-meta').find_all('a')[-1]
            
            movie_url = movie_link_tag['href']
            movie_name = movie_title_tag.text.strip().replace('《', '').replace('》', '')
            
            movies.append({'电影名称': movie_name, 'url': movie_url})
            
        # 指定文件名
        file_name = './static/upload/movie.json'

        # 使用 with 语句确保文件正确关闭
        with open(os.path.join(file_name), 'w', encoding='utf-8') as file:
            # 使用 json.dump 将 Python 对象转换为 JSON 格式并写入文件
            json.dump(movies, file, ensure_ascii=False, indent=4)

        print(f"数据已成功写入 {file_name} 文件")
        
        # data = getdoc(file_name)
        # print(data)
        # 导入所需的模块和类
        from langchain.embeddings import CacheBackedEmbeddings
        from langchain.storage import LocalFileStore
        from langchain_community.document_loaders import TextLoader
        from langchain_community.vectorstores import FAISS
        from langchain.embeddings.dashscope import DashScopeEmbeddings

        from langchain_text_splitters import CharacterTextSplitter
        
        # 实例化向量嵌入器
        embeddings = DashScopeEmbeddings()
        
        # 初始化缓存存储器
        store = LocalFileStore("./cache/")
        
        # 创建缓存支持的嵌入器
        cached_embedder = CacheBackedEmbeddings.from_bytes_store( embeddings, store, namespace=embeddings.model)
        
        # 加载文档并将其拆分成片段
        doc = TextLoader(file_name,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
        # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        faissdb.add(chunks,'movielist')
        return Response({"code":200})
    
    def post(self,request):
        ask = "电影"
        res = faissdb.search(ask,'movielist',4)
       
        prompt = "请帮我从以下{res}中返回三部电影的名称和请求地址,返回格式转成json格式返回,返回格式转成json格式返回,只返回json数据，不要任务描述信息"
        promptTemplate = PromptTemplate.from_template(prompt)
        # 生成prompt
        prompt = promptTemplate.format(res=res)
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt)
        data = json.loads(ret)
        print(data)
        return Response({"code":200,'data':data})
        
class TestFasiss(APIView):
    def get(self,request):
        res = requests.post("http://localhost:8000/test/")
        # print(res.json())
        return Response({"code":200})
    

import random
from http import HTTPStatus
# 建议dashscope SDK 的版本 >= 1.14.0
from dashscope import Generation
import requests
from tools.faissdb import faissdb

#把message存入redis,post中重构message，从redis中获取message
from http import HTTPStatus    
messages = [{'role': 'system', 'content': 'You are a helpful doctor.'}]  
from dashscope import Generation
          
class Ask(APIView):
    def post(self,request):
        user_input = request.data['askmes']  # 调用函数获取用户输入  
        messages.append({'role': 'user', 'content': user_input})  
        response = Generation.call(model="qwen-turbo",  
                                messages=messages,  
                                result_format='message')  
    
        if response.status_code == HTTPStatus.OK:  
            print(response.output.choices[0]['message']['content'])  # 直接打印回复内容  
            messages.append({'role': 'assistant',  # 假设这里我们假设回复的role是'assistant'  
                            'content': response.output.choices[0]['message']['content']})  
           
            return Response({"code":200,'mes':response.output.choices[0]['message']['content']})
        else:  
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (  
                response.request_id, response.status_code,  
                response.code, response.message  
            )) 
            
class StreamAsk(APIView):
    def get(self,request):
        ask = request.GET.get('mes')
        messages = [
        {'role': 'user', 'content': ask}]
        responses = Generation.call(model="qwen-turbo",
                                    messages=messages,
                                    result_format='message',  # 设置输出为'message'格式
                                    stream=True,  # 设置输出方式为流式输出
                                    incremental_output=True  # 增量式流式输出
                                    )
        
        for response in responses:
            if response.status_code == HTTPStatus.OK:
                print(response.output.choices[0]['message']['content'], end='')
                
            else:
                print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                    response.request_id, response.status_code,
                    response.code, response.message
                ))
                
        return Response({"code":200})
    
    
    
from django.http import StreamingHttpResponse


from dashscope import Generation
from datetime import datetime
import random
import json


# 定义工具列表，模型在选择使用哪个工具时会参考工具的name和description
tools = [
    # 工具1 获取当前时刻的时间
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "当你想知道现在的时间时非常有用。",
            "parameters": {}  # 因为获取当前时间无需输入参数，因此parameters为空字典
        }
    },  
   # 工具1 获取当前时刻的时间
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "当你想知道现订单信息非常有用。",
            "parameters": {}  # 因为获取当前时间无需输入参数，因此parameters为空字典
        }
    },  
    # 工具2 获取指定城市的天气
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "当你想查询指定城市的天气时非常有用。",
            "parameters": {  # 查询天气时需要提供位置，因此参数设置为location
                        "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或县区，比如北京市、杭州市、余杭区等。"
                    }
                }
            },
            "required": [
                "location"
            ]
        }
    }
]

# 模拟天气查询工具。返回结果示例：“北京今天是晴天。”
def get_current_weather(location):
    #调用天气预报的接口
    return f"{location}今天是晴天。 "

# 查询当前时间的工具。返回结果示例：“当前时间：2024-04-15 17:15:18。“
def get_current_time():
    # 获取当前日期和时间
    current_datetime = datetime.now()
    # 格式化当前日期和时间
    formatted_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    # 返回格式化后的当前时间
    return f"当前时间：{formatted_time}。"
  
def get_order_status():
    return "订单号为1001，已经支付"

# 封装模型响应函数
def get_response(messages):
    response = Generation.call(
        model='qwen-max',
        messages=messages,
        tools=tools,
        seed=random.randint(1, 10000),  # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
        result_format='message'  # 将输出设置为message形式
    )
    return response

class ToolsView(APIView):
    def get(self,request):
        mes = request.GET.get('mes')
        messages = [
                {
                    "content": mes,  # 提问示例："现在几点了？" "一个小时后几点" "北京天气如何？"
                    "role": "user"
                }
        ]
        
        # 模型的第一轮调用
        first_response = get_response(messages)
        assistant_output = first_response.output.choices[0].message
        print(f"\n大模型第一轮输出信息：{first_response}\n")
        messages.append(assistant_output)
        if 'tool_calls' not in assistant_output:  # 如果模型判断无需调用工具，则将assistant的回复直接打印出来，无需进行模型的第二轮调用
            print(f"最终答案：{assistant_output.content}")
            return
        # 如果模型选择的工具是get_current_weather
        elif assistant_output.tool_calls[0]['function']['name'] == 'get_current_weather':
            tool_info = {"name": "get_current_weather", "role":"tool"}
            location = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['location']
            tool_info['content'] = get_current_weather(location)
        # 如果模型选择的工具是get_current_time
        elif assistant_output.tool_calls[0]['function']['name'] == 'get_current_time':
            tool_info = {"name": "get_current_time", "role":"tool"}
            tool_info['content'] = get_current_time()
        elif assistant_output.tool_calls[0]['function']['name'] == 'get_order_status':
            tool_info = {"name": "get_order_status", "role":"tool"}
            tool_info['content'] = get_order_status()
        print(f"工具输出信息：{tool_info['content']}\n")
        messages.append(tool_info)
       
        # 模型的第二轮调用，对工具的输出进行总结
        second_response = get_response(messages)
        print(f"大模型第二轮输出信息：{second_response}\n")
        # print(f"最终答案：{second_response.output.choices[0].message['content']}")
        return Response({"code":200,'mes':second_response.output.choices[0].message['content']})
    
    
#1创建一张订单表，字段为订单号，时间，总金额，描述信息
#2.给表加一些测试数据
#写义2个工具类，
# 一个工具类是处理订单的问题，获取到参数‘订单号’查询订单表返回订单信息
#定义一个工具类，调用天气预报接口获取到天气信息
#定义一个工具类，调用百度api接口身份证验证

# myapp/views.py

import time
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET 
messages = [{'role': 'system', 'content': '你是一个百科可以回答各种问题'}]  

def generate_sse(responses):
   
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            data1 = response.output.choices[0]['message']['content']
            data = f"data: {data1}\n\n"
            print("####")
            if data1:
                yield data.encode('utf-8')  # 必须编码为字节串
            else:
                return "no mes"
    
     
@require_GET
def sse_view(request):
    user_input = request.GET.get('ask')  # 调用函数获取用户输入   
    messages.append({'role': 'user', 'content': user_input})  

    responses = Generation.call(model="qwen-turbo",  
                            messages=messages,  
                            result_format='message',
                            stream=True,  # 设置输出方式为流式输出
                            incremental_output=True  # 增量式流式输出
                            ) 
   
    response = StreamingHttpResponse(
        generate_sse(responses),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    return response
   

#获取天气信息接口
def get_current_weather(city):
    res = requests.get('http://apis.juhe.cn/simpleWeather/query',params={"city":city,"key":"545cf0bec2b0682dcc2c8f68325cf6c4"},headers={"Content-Type":"application/x-www-form-urlencoded"})
    data = json.loads(res.text)
    return data['result']['realtime']['temperature']
#查询订单
def getorders(orderno):
    orders = Torders.objects.filter(orderno=orderno).first()
    return {"orderno":orderno,'desc':orders.descip}


# 定义工具列表，模型在选择使用哪个工具时会参考工具的name和description
tools = [
    # 工具2 获取指定城市的天气
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "当你想查询指定城市的天气时非常有用。",
            "parameters": {  # 查询天气时需要提供位置，因此参数设置为location
                        "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或县区，比如北京、杭州、余杭区等。"
                    }
                }
            },
            "required": [
                "location"
            ]
        }
    },
    # 工具2 获取订单信息
    {
        "type": "function",
        "function": {
            "name": "getorders",
            "description": "当你想查询订单时非常有用。",
            "parameters": {  # 查询天气时需要提供位置，因此参数设置为location
                        "type": "object",
                "properties": {
                    "orderno": {
                        "type": "string",
                        "description": "获取订单号"
                    }
                }
            },
            "required": [
                "orderno"
            ]
        }
    }
]

# 封装模型响应函数
def get_response(messages):
    response = Generation.call(
        model='qwen-max',
        messages=messages,
        tools=tools,
        seed=random.randint(1, 10000),  # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
        result_format='message'  # 将输出设置为message形式
    )
    return response

class ToolsCall(APIView):
    def get(self,request):
        mes = request.GET.get('mes')
        messages = [
            {
                "content": mes,  # 提问示例："现在几点了？" "一个小时后几点" "北京天气如何？"
                "role": "user"
            }
        ]
    
        # 模型的第一轮调用
        first_response = get_response(messages)
        assistant_output = first_response.output.choices[0].message
        print(f"\n大模型第一轮输出信息：{first_response}\n")
        messages.append(assistant_output)
        if 'tool_calls' not in assistant_output:  # 如果模型判断无需调用工具，则将assistant的回复直接打印出来，无需进行模型的第二轮调用
            print(f"最终答案：{assistant_output.content}")
            return Response({"code":200,'mes':assistant_output.content})
        # 如果模型选择的工具是get_current_weather
        elif assistant_output.tool_calls[0]['function']['name'] == 'get_current_weather':
            tool_info = {"name": "get_current_weather", "role":"tool"}
            location = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['location']
            tool_info['content'] = get_current_weather(location)
        # 如果模型选择的工具是get_current_time
        elif assistant_output.tool_calls[0]['function']['name'] == 'getorders':
            tool_info = {"name": "getorders", "role":"tool"}
            orderno = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['orderno']
            tool_info['content'] = getorders(orderno)
        print(f"工具输出信息：{tool_info['content']}\n")
        messages.append(tool_info)

        # 模型的第二轮调用，对工具的输出进行总结
        second_response = get_response(messages)
        print(f"大模型第二轮输出信息：{second_response}\n")
        print(f"最终答案：{second_response.output.choices[0].message['content']}")
        return Response({"code":200,'mes':second_response.output.choices[0].message['content']})

def event_stream():
        while True:
            orders = Torders.objects.all()
            # list = [{"id":i.id,'orderno':i.orderno} for i in orders]
            list = json.dumps({"orderlist":[i.orderno for i in orders],"countlist":[100,200,300]})
            # 发送数据给客户端
            yield f"data: {list}\n\n"
    
            time.sleep(1)  # 每秒发送一次
@require_GET
def sse_views(request):
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response

import random
class RandromCount(APIView):
    def get(self,request):
        #获取列表
        olist = request.GET.get('olist')
        #定义一个温度列表
        nlist = []
        for i in olist:
            nlist.append(random.randint(10,100))
        return nlist

def getdata(olist):
        #获取列表
        # olist = request.GET.get('olist')
        #定义一个温度列表
        nlist = []
        for i in olist:
            nlist.append(random.randint(10,100))
        return nlist    

def get_data():
    while True:
        orderlist = ['1001','1002','1003']
        # data = requests.get('http://localhost:8000/randromCount/',params={"olist":orderlist})
        #设备对应的温度
        numberlist = getdata(orderlist)
        print(numberlist)#[10,20,30]
        errormes = ""
        # for (i,index) in enumerate(orderlist):
        #     #查询数据库，获取当前设备的正常范围值
        #     ovalue = OrdersValue.objects.filter(orderno=i).first()
        #     if numberlist[index]<ovalue.min or numberlist[index]>ovalue.max:
        #         errormes = errormes + "号码为"+i+"的目前温度为"+numberlist[index]+",出现异常，请关注"
            
            
        list = json.dumps({"orderlist":orderlist,"numberlist":numberlist,'errormes':errormes})
        yield f"data: {list}\n\n"
        time.sleep(3)
        
@require_GET
def echartssse(request):
    response = StreamingHttpResponse(get_data(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response
from .ser import *
import dashscope
class TestInterface(APIView):
    def get(self,request):
        # messages = [{'role': 'system', 'content': '你是一个非常厉害的文本规划师，请帮我对内容进行处理,返回前20个字'},
        #         {'role': 'user', 'content': '春天，四季之首，万物复苏的季节。温暖的阳光驱散了冬日的寒冷，大地披上了嫩绿的新装。花儿竞相开放，桃花、樱花、郁金香争奇斗艳，散发出阵阵芳香。小鸟在枝头欢快地歌唱，仿佛在庆祝新生的到来。人们脱去厚重的冬装，走出家门，享受着温暖的阳光和清新的空气。春天不仅带来了生机与活力，也带来了希望与梦想，让人心情愉悦，充满力量'}]

        # response = dashscope.Generation.call(
        #     dashscope.Generation.Models.qwen_turbo,
        #     messages=messages,
        #     result_format='message',  # 将返回结果格式设置为 message
        # )
        # if response.status_code == HTTPStatus.OK:
        #     print(response.output.choices[0].message.content)
        # else:
        #     print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
        #         response.request_id, response.status_code,
        #         response.code, response.message
        #     ))
        
        # res = requests.post("http://localhost:8000/cates/")
        # print(res.text)
        # ask = request.GET.get('ask')
        #exclude
        # res = Questions.objects.filter(ask__startswith=ask).all()
        # ser = QuestionsSer(res,many=True)
        return Response({"code":222,'data':'data'})
#添加分类接口
class CatesView(APIView):
    def post(self,request):
        # code = "h" +str(random.randint(100,999))
        #查询name为空的
        cates = Cates.objects.filter(name__isnull=True).first()
        if not cates:
            cates = Cates.objects.create()
        return Response({"code":200,'cateid':cates.id})
    
    def get(self,request):
        #获取搜索的名称
        sname = request.GET.get('sname')
        if sname:
            cates = Cates.objects.exclude(name__isnull=True).filter(name__startswith=sname).order_by('-add_time').all()[0:10]
        else:
            cates = Cates.objects.exclude(name__isnull=True).order_by('-add_time').all()[0:10]
        ser = CatesSer(cates,many=True)
        return Response({"code":200,'clist':ser.data})
    
#把调用模型回答封装成方法
def getmesbymodels(messages):
    
    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
    )
    mes=''
    if response.status_code == HTTPStatus.OK:
        mes=response.output.choices[0].message.content
    return mes
        
from .ser import *
#添加消息接口
class QuestionsView(APIView):
    def post(self,request):
        #接收参数
        ask = request.data['ask']
        cateid = request.data['cateid']
        #调用模型获取答案
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': ask}]
        answer = getmesbymodels(messages)
        #判断是否需要更新分类名称
        cates = Cates.objects.filter(id=cateid).first()
        cname = ''
        if not cates.name:
            #如果需要调用模型从ask中获取20个字符
            # mess = [{'role': 'system', 'content': '你是一个非常厉害的文本规划师，从角色为user的content中截取前3个字返回'},
            #     {'role': 'user', 'content': ask}]
            cname = ask[:10]
            cates.name = cname
            cates.save()
        #写入问答表
        Questions.objects.create(ask=ask,answer=answer,cid_id=cateid)
        
        return Response({"code":200,'catename':cname,'answer':answer})
    def get(self,request):
        #获取参数cateid
        cid = request.GET.get('cateid')
        #获取此分类下所有的问题
        ques = Questions.objects.filter(cid_id=cid).all()
        #调用序列化器处理
        ser = QuestionsSer(ques,many=True)
        #返回
        return Response({"code":200,'qlist':ser.data})
    
#批量删除  
class Catesall(APIView):
    def post(self,request):
        ids = request.data['ids']
        Cates.objects.filter(id__in=ids).delete()
        return Response({"code":200})
# 1导入prompt的类
from langchain.prompts import PromptTemplate
# 导入通义大模型
from langchain_community.llms import Tongyi
def getCates(mes):
    # 定义一个模板
    pp = "目前有三个分类，A:好评，B:中评，C:差评，请你对以下信息{mes}进行评价，返回分类,只返回字母"
    # 实例化模板类
    promptTemplate = PromptTemplate.from_template(pp)
    # 输入
    input = "这个洗地机拖地不干净，不方便"
    # 生成prompt
    prompt = promptTemplate.format(mes=mes)
    
    # 实例化通义大模型
    tongyi = Tongyi()
    ret = tongyi.invoke(prompt)
    return ret

class CommentView(APIView):
    def post(self,request):
        #获取参数 userid gid message
        userid = request.data['userid']
        gid = request.data['gid']
        message = request.data['message']
        level = getCates(message)
        data = {"userid":userid,"goodsid":gid,'message':message,'level':level}
        ser = CommentSer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"code":200})
        else:
            print(ser.errors)
            return Response({"code":10010,'mess':ser.errors})


class DDUrl(APIView):
    def get(self,request):
        redicturl = "http://127.0.0.1:8000/ddcallback/"
        cid = "dingiovq0d3pjsfj8222"
        url = "https://login.dingtalk.com/oauth2/auth?redirect_uri=%s&response_type=code&client_id=%s&scope=openid&state=dddd&prompt=consent"%(redicturl,cid)
        return Response({"code":200,'url':url})
    
    
class DDcallback(APIView):
    def get(self,request):
        #获取code
        authCode = request.query_params.get('code')

        # 根据authCode获取用户accessToken
        data = {
            "clientId": "dingiovq0d3pjsfj8222",
            "clientSecret": "gFVW1sn3Os1w4McptVJ0B1QxSFArEUAx58GiiVAU-wCQhXIll03pzAiM6Ept_24Q",
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
        
        #获取token
        #调用用户接口获取用户信息uid mobile
        # sfusers = Sflogin.objects.filter(uid=uid).first()
        # userid = sfusers.userid
        # if not sfusers:
        #     users = Tusers.objects.create(mobile=phone,nikename=name)
        #     userid = users.id
        #     Sflogin.objects.create(userid=users.id,uid=uid,types='dingding')
        # data={"userid":userid,'time':int(time.time())}
        # token = myjwt.jwt_encode(data)
            
        #根据uid查询三方登录表，如果存在取出userid，
        #如果不存在，用mobile写入用户表，把userid和uid写入三方登录表
        #调用jwt生成token,HttpResponseRedirect重定向到vue中转页面
        token = "123"
        userid=1
        return HttpResponseRedirect("http://localhost:5173/updatetoken?token="+token+"&userid="+str(userid))
    

from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
           
class TestSMM(APIView):
    def get(self,request):
        goods = Goods.objects.all()
        #假设已经有这么多的提示词示例组：
        examples =  [{"id": str(i.id), "features": i.tags} for i in goods]
       
        # #构造提示词模板
        example_prompt = PromptTemplate(
            input_variables=["id","features"],
            template="{id},"
        )
       
        # #调用MMR
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

        # #使用小样本提示词模版来实现动态示例的调用
        dynamic_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix="",
            suffix="",
            input_variables=["word"]
        )
        #查询用户浏览记录表，获取前5条 tags
        res = dynamic_prompt.format(word="时尚")
        items = res.split(',')
        ids = [int(item.strip()) for item in items if item.strip()]
        # #查询我游览过的[3,2,1]
        vlist = [1,2,4]
        difference = list(filter(lambda x: x not in vlist, ids))
        print(difference)  # 输出: [1]
        goods = Goods.objects.filter(id__in=difference).all()
        
        return Response({"code":200})
    
import requests  
class MovieData(APIView):
    def get(self,request):
        res = requests.get('https://movie.douban.com/',headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
        print(res.text)
        return Response({"code":200})