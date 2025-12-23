from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    Skills = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    time = models.CharField(max_length=200)
# Create your models here.
