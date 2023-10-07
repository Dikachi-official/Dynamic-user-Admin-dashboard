from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=400, unique=True)
    password = models.CharField(max_length=300)
