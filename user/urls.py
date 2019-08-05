from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('login.html',views.loginView,name='login'),
    path('register.html', views.registerView,name='register'),
    path('setpassword.html',views.setpasswordView,name='setpassword'),
    path('logout.html',views.logoutView,name='logout'),
]