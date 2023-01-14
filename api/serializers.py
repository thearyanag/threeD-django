from dataclasses import fields
from rest_framework import serializers
from api.models import Category,Assets,UserAssets

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryId' , 'CategoryName' , 'CategoryDescription')

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('AssetId' , 'AssetName' , 'Category' , 'FileName')

class UserAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssets
        fields = ('UserAssetsId' , 'UserId' , 'AssetId')