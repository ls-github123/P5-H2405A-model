from rest_framework.serializers import ModelSerializer
from .models import *

class SubDeptSer(ModelSerializer):
    class Meta:
        model=DepartMent
        fields=('id','name')

class DeptSer(ModelSerializer):
    child = SubDeptSer(many=True)
    class Meta:
        model=DepartMent
        fields=('id','name','child')
        
class OrdersSer(ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"