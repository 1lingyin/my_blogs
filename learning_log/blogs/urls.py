from django.conf.urls import url

from  . import views

urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),
    url(r'^topics/$',views.topics,name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    url(r'^new_topics/$',views.new_topics,name = 'new_topics'),
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name = 'new_entry'),

]
app_name = 'blogs'