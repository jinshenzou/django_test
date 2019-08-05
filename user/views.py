from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
# 登陆
def loginView(request):
    title = '登陆'
    unit_2 = '/user/register.html'
    unit_2_name = '立即注册'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username,password=password):
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    return render(request, 'user.html', locals())

# 注册
def registerView(request):
    return render(request)

# 修改密码
def setpasswordView(request):
    return render(request)

# 登出
def logoutView(request):
    return render(request)