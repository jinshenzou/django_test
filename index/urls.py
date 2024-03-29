from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    #path('<year>/<int:month>/<slug:day>',views.mydate),
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),
    # 参数为字典的URL
    re_path('dict/(?P<year>[0-9]{4}).html', views.myyear_dict, {'month':'05'}, name='myyear_dict'),
    # 带参数name的URL
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    path('download.html', views.download),
    path('index/', views.ProductList.as_view),
    path('test/',views.test),
    path('<int:id>.html', views.model_index)
]