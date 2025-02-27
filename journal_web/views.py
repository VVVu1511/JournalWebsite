from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
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
    """Show 1 topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    
    return render(request,'journal_web/topic.html',context) 

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_web:topics')
    context = {'form':form}
    
    return render(request,'journal_web/new_topic.html',context)