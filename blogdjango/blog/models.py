from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    imageURL = models.URLField(default = 'https://www.ncenet.com/wp-content/uploads/2020/04/No-image-found.jpg')
    datetime = models.DateTimeField(auto_now_add=True)
    body  = models.TextField()
    category = models.ManyToManyField(Category, default="Treino")

    def __str__(self):
        return self.title + ' | ' + str(self.author.first_name) + '  ' + str(self.author.last_name)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    body  = models.TextField()

    def __str__(self):
        return '%s - %s' %(self.post.title, self.author)