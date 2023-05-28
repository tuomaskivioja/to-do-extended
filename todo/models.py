from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name
