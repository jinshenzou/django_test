from django.db import models

# Create your models here.
# 创建产品分类表
class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)
# 创建产品信息表
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
# 一对一关系
class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)
class Performer_info(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)