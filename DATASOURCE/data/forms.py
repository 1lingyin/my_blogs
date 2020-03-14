from django import forms
from .models import datacollect
class form(forms.ModelForm):
    class Meta:
        model=datacollect
        fields = ['date','cities','level']
        labels = {'date':'','cities':'','level':''}