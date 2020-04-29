from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    subscription = models.CharField(max_length=10, default='free')

    def __str__(self):
        return self.user.username
