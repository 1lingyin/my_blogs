from django import forms
from .models import datacollect,data_c
class form(forms.ModelForm):
    class Meta:
        model=datacollect
        fields = ['date','cities','level']
        labels = {'date':'','cities':'','level':''}

class data_form(forms.ModelForm):
    class Meta:
        model=data_c
        fields = ['city','province','level','disease','time']
        labels = {'city':'','province':'','level':'','disease':'','time':''}