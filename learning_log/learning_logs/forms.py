from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields = ['text']
        labels = {'text': ''}
        widgets={'text':forms.Textarea(attrs={'cols':80})} #文本区域的宽度设为80列，而不是默认的40列
