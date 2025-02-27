from django.urls import path
from . import views

app_name = 'journal_web'

urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    #Page that shows all topics
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),  
]