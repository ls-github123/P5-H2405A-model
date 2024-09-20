from django.shortcuts import render
# from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class Test(APIView):
    def get(self,request):
        return Response({"code":200,'mes':'success'})
    

import random
from http import HTTPStatus
# 建议dashscope SDK 的版本 >= 1.14.0
from dashscope import Generation
import requests

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


