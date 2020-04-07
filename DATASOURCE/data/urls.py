from django.conf.urls import url

from  . import views

urlpatterns = [
    url(r'^add/$',views.add,name='add'),
    url(r"^advice/$", views.Advice, name="Advice")
]
app_name='data'