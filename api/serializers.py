from dataclasses import fields
from rest_framework import serializers
from api.models import Category,ThreeDModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId' , 'CategoryName')

class ThreeDModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeDModel
        fields = ('ThreeDId' , 'ModelName' , 'Category' , 'ThreeDModelFileName')