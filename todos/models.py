from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import BigAutoField

# Create your models here.

# User = get_user_model()

# class Todo(models.Model):
#     # id = models.Field(BigAutoField, primary_key=True, auto_created=True)
#     task = models.TextField(max_length=255)
#     doDate = models.DateTimeField(null=True)
#     isDone = models.BooleanField(default=False)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     updatedAt = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)

    def __self__(self):
        return self.title