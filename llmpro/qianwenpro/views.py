from django.shortcuts import render
# from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class Test(APIView):
    def get(self,request):
        return Response({"code":200,'mes':'success'})
