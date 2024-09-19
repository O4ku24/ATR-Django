from django.db import models
from django import forms


class Users(models.Model):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    post = models.CharField(max_length=20)

class Task(models.Model):
    
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    executioner = models.CharField(max_length=20)
    direct = models.CharField(max_length=20)
    description = models.TextField()
    startTime = models.DateTimeField(auto_now=True)
    endTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    