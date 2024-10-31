from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
# from  rest_framework import serializers

class TestRoleSer(ModelSerializer):
    class Meta:
        model = TestRole
        fields=('id','name')
        
        
class ResourceSer(ModelSerializer):
    
    name = serializers.CharField(required=True)
    pid = serializers.IntegerField()
    
    def validate_name(self, data):
        """
        validate_<字段名>  # 针对指定字段进行验证
        # validate_mobile 表示 针对mobile字段进行单独的校验，mobile也可以换成其他字段。
        """
        print("data=", data)
        ret = Resource.objects.filter(name=data).first()
        if ret:
            raise serializers.ValidationError(code="name", detail="当前用户名已经被注册！")
        return data  # 必须把数据返回，否则后续操作中序列化器无法获取校验后的结果
    class Meta:
        model = Resource
        fields="__all__"
        
        
class RolesSer(ModelSerializer):
    class Meta:
        model = Roles
        fields="__all__"