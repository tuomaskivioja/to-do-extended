from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey

# Create your models here.

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()