from django.urls import re_path
from . import views
from .views import *
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),      #第一个d+为类型的id, 第二个为当前是第几页,第三个是排序的依据
    re_path(r'^(\d+)/$', views.detail, name='detail'),     #详细页
    re_path(r'^search/$',MySearchView()),
    # url(r'^list/$', views.list, name='list'),
]
