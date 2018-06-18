"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
app_name='learning_logs'
urlpatterns=[
    url(r'^topics/$',views.index,name='topics'),
    url(r'^$',views.index,name='index'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #用于编辑条目的页面
    url(r'^edit/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'), #URL模式
       ]