from django.db import models

class TodoItem(models.Model):
    content = models.TextField()

class TodoItemHistory(models.Model):
    content = models.TextField()
