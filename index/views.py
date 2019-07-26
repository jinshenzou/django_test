from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import Product
# Create your views here.
def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    context = {
        'title':'首页',
        'type_list':type_list,
        'name_list':name_list,
    }
    return render(request,'index.html',context=context,status=200)

def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

def myyear(request, year):
    return render(request,'myyear.html')

def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month':month})

def download(request):
    respone = HttpResponse(content_type='text/csv')
    respone['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(respone)
    writer.writerow(['Fist row', 'A', 'B', 'C'])
    return respone

def login(request):
    # 相对路径，代表首页地址
    return redirect('/')