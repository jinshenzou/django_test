from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import Product,Type
# Create your views here.
def index(request):
    type_list = Product.objects.values('type__type').distinct()
    name_list = Product.objects.values('name','type__type')
    username = request.user.username
    return render(request,'index.html',context=locals(),status=200)

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
    if request.method == 'POST':
        name = request.POST.get('name')
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('username is '+name)
    return redirect('/')

from django.views.generic import ListView
class ProductList(ListView):
    context_object_name = 'type_list'
    template_name = 'index.html'
    queryset = Product.objects.values('type').distinct()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name','type')
        return context

def test(request):
    return render(request,'test.html',{'title':'测试'})

from .form import *
def index1(request):
    # GET请求
    if request.method == 'GET':
        product = ProductForm()
        return render(request,'data_form.html',locals())
    # POST请求
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            # 获取网页控件name的数据
            # 方法一
            name = product['name']
            # 方法二
            cname = product.cleaned_data['name']
            return HttpResponse(name+'提交成功')
        else:
            # 将错误信息输出
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())

def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        # 判断数据是否存在
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            # 获取weight的数据，并通过clean_weight进行清洗，转换成Python数据类型
            weight = product.cleaned_data['weight']
            # 数据保存方法一
            # 直接将数据保存到数据库
            product.save()
            # 数据保存方法二
            # save方法设置commit=False，将生成数据库对象product_db，然后对该对象属性值修改并保存
            # product_db = product.save(commit=False)
            # product_db.name = '我的iPhone'
            # product_db.save()
            # 数据保存方法三
            # save_m2m()方法用于保存ManyToMant的数据模型
            # product.save_m2m()
            return HttpResponse('提交成功！weight清洗后的数据为：'+weight)
        else:
            # 将错误信息输出,error_msg是将错误信息以json格式输出
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())