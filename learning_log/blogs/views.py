from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm
# Create your views here.
def index(request):
    topics=Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'blogs/index.html',context)

def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request, 'blogs/topics.html', context)
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request, 'blogs/topic.html', context)
def new_topics(request):
    #添加主题
    if request.method !='POST':
        #如果没有提交表单就新建一个表单
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topics'))
    context={'form':form}
    return render(request,'blogs/new_topics.html',context)
