from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return  f"Tweet nick: {self.username} message: {self.message} date: {self.timestamp}"
