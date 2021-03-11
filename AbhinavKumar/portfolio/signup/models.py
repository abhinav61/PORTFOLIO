from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    
    email = models.EmailField(max_length=100)
    page = models.CharField(max_length=50)
    summary = models.TextField()
    date = models.DateTimeField()

