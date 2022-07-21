from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager #for Post tags
from django.contrib.auth.models import User #for Comment

class Post(models.Model):
    title = models.CharField(max_length = 255) 
    description = models.CharField(max_length = 1000)
    content = models.TextField() 
    created_on = models.DateTimeField(default = timezone.now) 
    tags = TaggableManager()
    slug = models.SlugField(unique = True, blank = True, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/posts/{self.slug}'

class Comment(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default = timezone.now)
    for_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
