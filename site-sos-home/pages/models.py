from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(default='https://www.ncenet.com/wp-content/uploads/2020/04/No-image-found.jpg')

    def __str__(self):
        return self.name

