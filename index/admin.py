from django.contrib import admin

# Register your models here.
from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','weight','size','type']
    search_fields = ['id','name','type__type']
    list_filter = ['name','type__type']
    ordering =['id']
    fields = ['name','weight','size','type']
    #readonly_fields = ['name']
admin.site.register(Product,ProductAdmin)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','type']
admin.site.register(Type,TypeAdmin)