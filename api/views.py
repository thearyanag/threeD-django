import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from api.models import Category,Assets,UserAssets
from api.serializers import CategorySerializer,AssetSerializer

@csrf_exempt
def categoryApi(request,id=0):
    if request.method == "GET":
        category = Category.objects.all()
        category_serializer = CategorySerializer(category , many=True)
        return JsonResponse(category_serializer.data,safe=False)
    elif request.method == "POST":
        category_data = JSONParser().parse(request)
        print(category_data)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added successfully" , safe=False)
        return JsonResponse("Faild to add" , safe=False)
    elif request.method == "PUT":
        category_data = JSONParser().parse(request)
        category = Category.objects.get(CategoryId = category_data["CategoryId"])
        category_serializer = CategorySerializer(category , data=category_data)
        if category_serializer.is_valid():  
            category_serializer.save()
            return JsonResponse("Updated successfully" , safe=False)
        return JsonResponse("Faild to update" , safe=False)
    elif request.method == "DELETE":
        category = Category.objects.get(CategoryId = id)
        category.delete()
        return JsonResponse("Deleted Successfully" , safe=False)

@csrf_exempt
def threeDModelApi(request,id=0):
    if request.method == "GET":
        threeDModel = Assets.objects.all()
        threeD_serializer = AssetSerializer(threeDModel , many=True)
        return JsonResponse(threeD_serializer.data,safe=False)
    elif request.method == "POST":
        threeD_data = JSONParser().parse(request)
        print(threeD_data)
        threeD_serializer = AssetSerializer(data=threeD_data)
        if threeD_serializer.is_valid():
            threeD_serializer.save()
            return JsonResponse("Added successfully" , safe=False)
        return JsonResponse("Faild to add" , safe=False)
    elif request.method == "PUT":
        threeD_data = JSONParser().parse(request)
        threeDModel = Assets.objects.get(ThreeDId = threeD_data["ThreeDId"])
        threeD_serializer = AssetSerializer(threeDModel , data=threeD_data)
        if threeD_serializer.is_valid():
            threeD_serializer.save()
            return JsonResponse("Updated successfully" , safe=False)
        return JsonResponse("Faild to update" , safe=False)
    elif request.method == "DELETE":
        threeDModel = Assets.objects.get(ThreeDId = id)
        threeDModel.delete()
        return JsonResponse("Deleted Successfully" , safe=False)

@csrf_exempt
def saveModel(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name , file)
    return JsonResponse(file_name , safe=False)