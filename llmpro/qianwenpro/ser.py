from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

# class QuestionsSer(ModelSerializer):
#     add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
#     class Meta:
#         model = Questions
#         fields="__all__"

class QuestionsSer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ('ask','answer')
        
class CatesSer(ModelSerializer):
    class Meta:
        model = Cates
        fields = ('id','name')