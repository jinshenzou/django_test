from django.db import models

# Create your models here.
# 创建产品分类表
class Type(models.Model):
    id = models.AutoField('序号',primary_key=True)
    type = models.CharField('产品类型',max_length=20)
    def __str__(self):
        return self.type
    class Meta:
        verbose_name = '产品类型'
        verbose_name_plural = '产品类型'
# 创建产品信息表
class Product(models.Model):
    id = models.AutoField('序号',primary_key=True)
    name = models.CharField('名称',max_length=50)
    weight = models.CharField('重量',max_length=20)
    size = models.CharField('尺寸',max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,verbose_name='产品类型')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'
# 一对一关系
class Performer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)
class Performer_info(models.Model):
    id = models.AutoField(primary_key=True)
    performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)
# 一对多
class Program(models.Model):
    id = models.AutoField(primary_key=True)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)