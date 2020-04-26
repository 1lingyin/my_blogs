from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class datacollect(models.Model):
    date=models.CharField(max_length=20)
    cities=models.CharField(max_length=20)
    level=models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)
class data_c(models.Model):
    city=models.CharField(max_length=20)
    province=models.CharField(max_length=20)
    level=models.CharField(max_length=20)
    disease=models.CharField(max_length=20)
    time=models.DateField()

