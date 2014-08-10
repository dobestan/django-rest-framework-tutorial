from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, related_name = "posts")
    title = models.CharField(max_length = 255)
    content = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name = "comments")
    post = models.ForeignKey(Post, related_name = "comments")
    content = models.TextField()
