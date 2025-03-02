from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm,EntryForm
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


def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('journal_web:topic',topic_id=topic_id)
    context = {'topic':topic,'form': form}
    return render(request,'journal_web/new_entry.html',context)
