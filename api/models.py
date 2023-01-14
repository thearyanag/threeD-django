from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    CategoryDescription = models.CharField(max_length=100)
    OwnerAddress = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName

class Assets(models.Model):
    AssetId = models.AutoField(primary_key=True)
    AssetName = models.CharField(max_length=100)
    AssetDescription = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    FileName = models.CharField(max_length=100)  

    def __str__(self):
        return self.AssetName 

class UserAssets(models.Model):
    UserAssetsId = models.AutoField(primary_key=True)
    UserId = models.CharField(max_length=100)
    Asset = models.ForeignKey(Assets, on_delete=CASCADE)

    def __str__(self):
        return self.UserIds