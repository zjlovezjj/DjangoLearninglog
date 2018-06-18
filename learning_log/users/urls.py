"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login #导入默认视图
from . import views
app_name='users'
urlpatterns=[
    #登陆页面
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'register/$',views.register,name='register'),
]