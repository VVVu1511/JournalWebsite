from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """The home page for Journal Web"""
    return render(request,'journal_web/index.html')

def topics(request):
    """Show alls topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'journal_web/topics.html',context)   

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    
    return render(request,'journal_web/topic.html',context) 
    