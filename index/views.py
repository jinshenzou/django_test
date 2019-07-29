from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import Product
# Create your views here.
def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
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
        return HttpResponse('username is '+ name)
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
    return render(request,'test.html')