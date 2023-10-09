from django.db import models

# Create your models here.


class AdminUser(models.Model):
    name = models.CharField(max_length=400, unique=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name
