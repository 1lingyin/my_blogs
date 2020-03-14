from django.db import models

# Create your models here.
class datacollect(models.Model):
    date=models.CharField(max_length=20)
    cities=models.CharField(max_length=20)
    level=models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)