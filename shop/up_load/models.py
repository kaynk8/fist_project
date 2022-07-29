from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)