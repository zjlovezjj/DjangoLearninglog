from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200) #该属性存储少量文本
    date_added=models.DateTimeField(auto_now_add=True) #将此属性设为当前的日期和时间
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model): #添加条目定义模型
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        """返回模型的字符串表示"""
        return  self.text[:50]+"..."