from django.db import models

# Create your models here.


class AdminUser(models.Model):
    username = models.CharField(max_length=400, unique=True)
    password = models.CharField(max_length=300)

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
