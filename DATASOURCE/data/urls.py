from django.conf.urls import url

from  . import views

urlpatterns = [
    url(r'^add/$',views.add_data,name='add_data'),

]
app_name='data'