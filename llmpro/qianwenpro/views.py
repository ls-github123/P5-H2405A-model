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