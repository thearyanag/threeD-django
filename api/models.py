from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)

class ThreeDModel(models.Model):
    ThreeDId = models.AutoField(primary_key=True)
    ModelName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    ThreeDModelFileName = models.CharField(max_length=100)  