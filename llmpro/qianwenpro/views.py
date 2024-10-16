from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from tools.textload import getdoc
import os
# Create your views here.
from tools.faissdb import faissdb
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

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
        # 指定文件夹路径
        folder_path = './static/upload/'
        from langchain.document_loaders import DirectoryLoader
        # 使用 DirectoryLoader 加载文件夹中的所有文件
        loader = DirectoryLoader(folder_path, glob='**/*.txt')  # 根据需要调整文件类型
        documents = loader.load()

        # 检查加载的文档数量
        print(f'Loaded {len(documents)} documents from {folder_path}')

        # 将文档分割成小块（可选）
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        chunks = text_splitter.split_documents(documents)
        
       
        # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        faissdb.add(chunks,'mtlist')
        res = faissdb.search("电影",'mtlist',4)

        # 检查分割后的文本数量
        print(res)

        
        

        # ask = "电影"
        # res = faissdb.search(ask,'movielist',4)
       
        # prompt = "请帮我从以下{res}中返回三部电影的名称和请求地址,返回格式转成json格式返回,返回格式转成json格式返回,只返回json数据，不要任务描述信息"
        # promptTemplate = PromptTemplate.from_template(prompt)
        # # 生成prompt
        # prompt = promptTemplate.format(res=res)
        # tongyi = Tongyi()
        # ret = tongyi.invoke(prompt)
        # data = json.loads(ret)
        # print(data)
        # django文件上传
        #文件上传

        #获取参数
       
        # file = request.FILES.get('file')
        # print(file)
        # filename = file.name
        
        # with open(f'./static/upload/{filename}', 'wb') as f:
        #     for chunk in file.chunks():
        #         f.write(chunk)
        return Response({"code":200,'data':"data"})
        
class TestFasiss(APIView):
    def get(self,request):
        # res = requests.post("http://localhost:8000/test/")
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
    

def generate_sse_lcc(chunks):
       
    for chunk in chunks:
        data = f"{chunk.content}"
        if chunk:
            yield data.encode('gbk')
        else:
            print('____________')
            return 'no mes'
@require_GET
def sse_view(request):
    # user_input = request.GET.get('ask')  # 调用函数获取用户输入   
    # messages.append({'role': 'user', 'content': user_input})  

    # responses = Generation.call(model="qwen-turbo",  
    #                         messages=messages,  
    #                         result_format='message',
    #                         stream=True,  # 设置输出方式为流式输出
    #                         incremental_output=True  # 增量式流式输出
    #                         ) 
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_community.chat_models.tongyi import ChatTongyi


    chat = ChatTongyi()

    prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")


    chain = prompt | chat


    res = chain.stream({"topic": "熊"})

   
    response = StreamingHttpResponse(
        generate_sse_lcc(res),
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
    
    
class FileUpload(APIView):
    def post(self,request):
        #获取文件流
        file  = request.FILES.get('file')
        #获取文件名
        name = file.name
        #指定要上传的目录
        path = './static/upload/'+name
        #写入文件
        with open(os.path.join(path),'wb') as f:
            for i in file.chunks():
                f.write(i)
        return Response({"code":200})
    
    def get(self,request):
        # 指定文件夹路径
        folder_path = './static/upload/'
        from langchain.document_loaders import DirectoryLoader
        # 使用 DirectoryLoader 加载文件夹中的所有文件
        loader = DirectoryLoader(folder_path, glob='**/*.txt')  # 根据需要调整文件类型
        documents = loader.load()

        # 检查加载的文档数量
        print(f'Loaded {len(documents)} documents from {folder_path}')

        # 将文档分割成小块（可选）
        text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
        chunks = text_splitter.split_documents(documents)
       
        # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        faissdb.add(chunks,'alist')
        res = faissdb.search("电脑",'alist',4)

        # 检查分割后的文本数量
        print(res)
        return Response({"code":200})
    
    
def generate_sse_lc(chunks):
   
    for chunk in chunks:
        data = f"{chunk}"
        if chunk:
            yield data.encode('gbk')
        else:
            print('____________')
            return 'no mes'
        
            
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET           


@require_GET
def sse_notifications(request):
        query_text = request.GET.get('ask')  # 调用函数获取用户输入 
    
        # 实例化模板类
        pp = "帮我返回{res}中答案"
       
        promptTemplate = PromptTemplate.from_template(pp)
        prompt = promptTemplate.format(res=query_text)
         
            
        llm=Tongyi()
   
        chuns = llm.stream(prompt)
                   
        response = StreamingHttpResponse(
            generate_sse_lc(chuns),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        return response
    

import random
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 初始化 ConversationBufferMemory
memory = ConversationBufferMemory()

@require_GET
def qustions_ask(request):
        user_input = request.GET.get('ask')
        memory.chat_memory.add_user_message(user_input)
        
        llm = Tongyi()

        # 定义 Prompt 模板
        template = """请你设计一下成语接龙的游戏，用户输入一个成语,模型用最后一字生成一个新的成语，新成语的第一个字是上一个成语的最后一个字
        如果用户输入的是其他问题，先回答问题再提醒用户玩成语接龙游戏
        User: {input}
        AI: """

        prompt = PromptTemplate(input_variables=["history","input"], template=template)

        # 初始化 LLMChain
        chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
       
        
        # 将用户输入和 AI 响应添加到对话历史记录中
        res = chain.run(input=user_input)
        memory.chat_memory.add_ai_message(res)
       
       
        chuns = llm.stream(res)
                   
        response = StreamingHttpResponse(
            generate_sse_lc(chuns),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        return response
    
       


from langchain_community.llms import Tongyi
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
#多轮对话
class AskMessage(APIView):
    def post(self,request):
        ask = request.data['ask']
        memory.chat_memory.add_user_message(ask)
        memory.load_memory_variables({})
        
        llm = Tongyi(temperature=0)
        
         # 定义 Prompt 模板
        template = """这是一个成语接龙的游戏，用户输入一个成语，ai根据成语的最后一个字再组成一个成语。用户再根据
        ai的成语最后一个字输入成语，如果用户输入错误，提示用户游戏结果
        User: {input}
        AI: """

        prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
        
        res = chain.predict(input=ask)
        memory.chat_memory.add_ai_message(res)
        
        
        return Response({"code":200,'mes':res})
    

from langchain_community.document_loaders import TextLoader    

def orders_search(input:str)->str:
    #查询faiss
    
    return "订单号为"+input+"商品已发货，时间为2023-10-10"

def doctor_search(input:str)->str:
    #查询医生表
    return input +"是一个非常优秀的医生"
def faq(input:str)->str:
    #查询faiss
    print("input:"+input)
    res = faissdb.search(input,'ffile',1)
    return res

from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType
memory = ConversationBufferMemory(memory_key='chat_history',return_message=True)

from langchain.callbacks.base import BaseCallbackHandler

class StreamingCallbackHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # 每当从语言模型接收到新token时调用
        print("###")
        print(token, end='', flush=True)

    def on_tool_start(self, serialized, input_str, **kwargs) -> None:
        # 当工具开始执行时调用
        print(f"开始执行工具: {input_str}")

    def on_tool_end(self, output, **kwargs) -> None:
        # 当工具结束执行时调用
        print(f"工具执行完成: {output}")
        
class FUPload(APIView):
    def post(self,request):
        file = request.FILES['file']
        path = "./static/upload/"+file.name
        
        with open(os.path.join(path),'wb') as f:
            for i in file.chunks():
                f.write(i)
                
        # 加载文档并将其拆分成片段
        doc = TextLoader(path,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
        faissdb.add(chunks,'ffile')
        return Response({"code":200})
    def get(self,request):
        # res = faissdb.search("你今年多大了",'ffile',1)
        
        #模拟问电商faq
        question = request.GET.get('ask')
        tools=[
            Tool(name="search order",func=orders_search,
            description = "当用户咨询关于订单的问题用这个工具回答,从问答中截取订单号，只取订单号后面的号码"),
            Tool(name="doctor search",func=doctor_search,
            description = "当用户咨询关于医生的问题请用这个工具回答"),
            Tool(name="faq",func=faq,
            description = "当用户问除了订单和医生的其他咨询问题，比如年龄等问题都用这个工具回答"),
        ]
        llm = Tongyi()
        agent = initialize_agent(tools,llm,
                                 agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                 memory=memory,
                                verbose=True)
        res = agent.invoke(question)
        
        data = llm.stream(res['output'])
        
        response = StreamingHttpResponse(
            generate_sse_lc(data),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        return response
        
        # return Response({"code":200,'mes':res})
        
        
class TestFaiss(APIView):
    def get(self,request):
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
        # doc = TextLoader("./static/upload/a.txt",encoding='utf-8').load()
        # spliter = CharacterTextSplitter("\n",chunk_size=200, chunk_overlap=0)
        # chunks = spliter.split_documents(doc)
        # # 创建向量存储
        # db = FAISS.from_documents(chunks, cached_embedder)
        #以索引的方式保存
        # db.save_local("testfaiss")
        db = FAISS.load_local("testfaiss",cached_embedder,allow_dangerous_deserialization=True)
        res = db.similarity_search("我是谁", k=3)
        print(res)
        return Response({"code":200,'mes':res})




from tools.bdapi import bdapi
from langchain.chains.llm import LLMChain
from langchain_community.llms import Tongyi

llm = Tongyi()
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.transform import TransformChain
from langchain.chains.sequential import SimpleSequentialChain


 # 第一个任务
def transform_func(inputs:dict) -> dict:
    text = inputs["text"]
    mes=bdapi.audit_mes(text)
    return {"output_text":mes}
               
class TestBd(APIView):
    def get(self,request):
        mes = request.GET.get('mes')

        #文档转换链
        transform_chain = TransformChain(
            input_variables=["text"],
            output_variables=["output_text"],
            transform=transform_func
        )

        # 第二个任务
        template = """对下面的文字进行处理:
        如果内容为内容不合法直接返回这几个字，如果是别的
        内容请对内容做优化处理后返回,返回时只返回内容不返回描述信息,内容为
        {output_text}

        # # """
        # template = """对下面的文字进行总结:
        # {output_text}

        # 总结:"""

        prompt = PromptTemplate(
            input_variables=["output_text"],
            template=template
        )
        llm_chain = LLMChain(
            llm = Tongyi(),
            prompt=prompt
        )

        #使用顺序链连接起来
        squential_chain = SimpleSequentialChain(
            chains=[transform_chain,llm_chain],
            verbose=True
        )

        res = squential_chain.invoke(mes)
       
        
        if res  == "内容不合法":
            return Response({"code":10010,'data':res})
        else:
            #写入发布表
            return Response({"code":200,'data':res})
    
import random
from tools.mredis import mredis
class PublishView(APIView):
    def post(self,request):
        #获取参数
        #写入发布表
        # publish = Publish
        # #把生成id加入队列
        code = str(random.randint(1000,9999))
        mredis.list_add('dblist',code)
        #返回结果
        return Response({"code":200})
    
    def get(self,request):
        file_name = "/Users/hanxiaobai/Downloads/dxb/h2405a/llmpro/qianwenpro/a.txt"
        doc = TextLoader(file_name,encoding='utf-8').load()
        spliter = CharacterTextSplitter("\n",chunk_size=5, chunk_overlap=0)
        chunks = spliter.split_documents(doc)
       
        # faissdb.add(chunks,'llindex')
        res = faissdb.search('电影','llindex',3)
        # 定义一个模板
        pp = "对以下内容进行处理，以json格式返回内容。只返回json数据,不返回描述信息,也不返回json这个单词，内容为{mes}"
        # 实例化模板类
        promptTemplate = PromptTemplate.from_template(pp)
        # 生成prompt
        prompt = promptTemplate.format(mes=res)

        # 实例化通义大模型
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt)
        data = json.loads(ret)
        print(data)
        return Response({"code":200})
    
from django.db.models import Sum  
from datetime import datetime,timedelta

from django.core.mail import send_mail  
from llmpro import settings
def send_email_view(mail):  
    subject = '测试邮件主题'  
    message = '这是测试邮件的内容。'  
    from_email = settings.EMAIL_HOST_USER  # 可以是 settings.py 中的 EMAIL_FROM  
    to_email = [mail]  # 收件人邮箱地址列表  
  
    # 发送邮件  
    send_status = send_mail(subject, message, from_email, to_email, fail_silently=False)  
    print(send_status)
    return send_status
    
class CrmManager(APIView):
    def get(self,request):
        # 按客户分组并计算每个客户的总订单金额  
        # now = datetime.now()
        # pre = now - timedelta(days=9)
        # print(pre)
        # cates = Cates.objects.filter(add_time__lt=now,add_time__gt=pre).values('userid').annotate(total_amount=Sum('numbers')).order_by('total_amount')
        # for i in cates:
        #     print(i)
        # send_email_view("763005825@qq.com")
        
        end = datetime.now()
        #查询本月
        start = datetime.strftime(end,'%Y-%m-01')
        print(start)
        #30天前
        start = end - timedelta(days=30)
        # select sum(number) as tcount  from cates group by userid  order by tcount desc limit 0,10;
        cates = Cates.objects.filter(add_time__gte=start,add_time__lte=end).values("userid").annotate(tmoney=Sum('numbers')).order_by('-tmoney')[0:10]
        print(cates)
        return Response({"code":200}) 

import pandas as pd
class TestCsv(APIView):
    def get(self,request):
        reslist = []
        data = pd.read_csv("/Users/hanxiaobai/Downloads/dxb/h2405a/llmpro/static/upload/reg.csv")
        for index, row in data.iterrows():  
            name = row[0]
            interface = "http://locahost:8000/"+row[1]
            params = row[2]
            rescode = row[3]
            res = requests.get(interface,params= params)
            data = json.loads(res.text())
            if data['code'] == rescode:
                result = 1
            else:
                result =2
                
            reslist.append({"name":name,'params':params,'result':result})
                
        return Response({"code":200,'res':reslist})
        
# #删除此角色对应的所有权限
# role.resource.clear()
# #添加新的权限
# role.resource.add(*values)
# for index,s in enumerate(reslist):

def resdata(data):
    if len(data)>0:
        parentlist = []
        ids = []
        for i in data:
            if i['pid'] not in ids:
                pdict = {"id":i['pid'],'label':i['pname'],'children':[]}
                parentlist.append(pdict)
                ids.append(i['pid'])
        
        for (index,i) in enumerate(parentlist):
            for j in data:
                if int(i['id']) == int(j['pid']):
                    parentlist[index]['children'].append({"id":j['id'],'label':j['name'],'url':j['url']})
            
        return parentlist
    else:
        return []

class ResourceView(APIView):
    def post(self,request):
        userid = request.data['userid']
        res = request.data['res']
        user = Customer.objects.filter(id=userid).first()
        #删除此用户所有的资源
        user.resource.clear()
        #把新的资源配制给用户
        user.resource.add(*res)
        return Response({"code":200})
    
    def get(self,request):
        userid = request.GET.get('userid')
        user = Customer.objects.filter(id=userid).first()
        user = user.resource.all()
        reslist = []
        for i in user:
            dict = {"id":i.id,'pid':i.pid.id,'pname':i.pid.name,'name':i.name,'url':i.url}
            reslist.append(dict)
        
        res = resdata(reslist)
        return Response({"code":200,"reslist":res})
from tools.myjwt import mjwt
import time
class LoginView(APIView):
    def post(self,request):
        name = request.data['name']
        pwd = request.data['pwd']
        print(name)
        print(pwd)
        users = Customer.objects.filter(account=name,password=pwd).first()
        print(users)
        if users:
            #登录成功生成token返回
            #查询资源列表，返回前端
            #判断用户角色redis中是否存在，如果存在返回
            #如果不存在查询
            roleid = users.roles.id
            key = 'roles'+str(roleid)
            mredis.str_del(key)
            resource = mredis.str_get(key) 
            user = {"id":users.name,'name':name,'exp':int(time.time())+3600}
            token = mjwt.jwt_encode(user)
            pomitionlist = []
            #查询redis
            if resource:
                resource = json.loads(resource)
                mlist = mredis.str_get('menulist'+str(roleid)) 
                pomitionlist = json.loads(mlist)
            else:
                res = users.roles.resources.all()
                reslist = []
                for i in res:
                    pomitionlist.append(i.url)
                    dict = {"id":i.id,'pid':i.pid.id,'pname':i.pid.name,'name':i.name,'url':i.url}
                    reslist.append(dict)
                resource = resdata(reslist)
                #存入redis
                mredis.str_set(key,json.dumps(resource))
                #根据pomitionlist查询另外表，查询接口权限，存入redis
                mredis.str_set('menulist'+str(roleid),json.dumps(pomitionlist))
                
                
            return Response({"code":200,'userid':users.id,'token':token,'menulist':resource,'pomitionlist':pomitionlist})
        else:
            return Response({"code":10010})