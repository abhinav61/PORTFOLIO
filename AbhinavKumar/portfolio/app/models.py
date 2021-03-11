from django.db import models

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class Data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    Project = models.TextField()

