from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AdminUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=400, unique=True)
    password = models.CharField(max_length=300)

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
