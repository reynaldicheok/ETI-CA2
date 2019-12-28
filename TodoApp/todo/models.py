from django.db import models
from datetime import date
from django.contrib.auth.models import User

class TodoItem(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        
    )

class TodoItemHistory(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
