from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rooms(models.Model):
    """The discussion room"""
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    participants = ... # a list of users
    # with another model
    posts = models.ForeignKey("Posts", on_delete=models.DO_NOTHING)
    settings = models.ForeignKey("Settings", on_delete=models.DO_NOTHING)
    


class Posts(models.Model):
    """Messages in the discussion room"""
    ...

class Settings(models.Model):
    """defines settings for a discussion room"""
    ...