from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    """The discussion room"""
    title = models.CharField(max_length=200) # title for the room
    description = models.TextField(null=True) # description of the room
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    participants = ... # participants in the room
    # with another model
    posts = models.ForeignKey("Post", on_delete=models.DO_NOTHING) # list messages in the room
    setup = models.ForeignKey("Settings", on_delete=models.DO_NOTHING) # public, private or restricted to some users
    status = models.CharField(max_length=20) # active, archived or closed
    
    def __str__(self):
        return str(self.title,'---', self.description)
    
    

class Topic(models.Model):
    
    topic = models.CharField(max_length=200) # topic for discussion
    description = models.TextField(null=True) # description of the topic
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.topic)
    
class Participant(models.Model):
    """participants"""
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user participating 
    # role = ... # creator, participant
    join_date = ... # data joined the discussion room/ topic
    last_activity_date = models.DateTimeField(auto_now_add=True)
    status = ... # active, muted, banned

    def __str__(self):
        return str(self.user)

    
class Post(models.Model): # messages model
    """Messages in the discussion room"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True) # date post created
    last_edited_data = models.DateTimeField(auto_now_add=True) # date last edited
    attachments = ... # files, images, etc..
    replies = models.ForeignKey("self", on_delete=models.CASCADE) # reference to message this replies
    
    def __str__(self):
        return str(self.author)

class Settings(models.Model):
    """defines settings for a discussion room"""
    roomsettings = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    notificationsettings = models.CharField(max_length=200)
    appearancesettings = ... # should be choices
    discussionsettings = ... # e.g allowed file types, message char limit
    
    def __str__(self):
        ... 