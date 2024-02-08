from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """topic info"""
    name=models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    
class Room(models.Model):
    """The discussion room"""
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True) # description of the room
    name = models.CharField(max_length=200) # name of the room
    created = models.DateTimeField(auto_now_add=True) # created once
    updated= models.DateTimeField(auto_now=True) # changed
    participants = ... # participants in the room
  
    
    def __str__(self):
        return str(self.name)
    
    
class Post(models.Model): # messages model
    """Messages in the discussion room"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True) # date post created
    last_edited_on= models.DateTimeField(auto_now=True) # date last edited
    
    
    def __str__(self):
        return str(self.author)

    
# class Participant(models.Model):
#     """participants"""
#     user = models.ForeignKey(User, on_delete=models.CASCADE) # user participating 
#     # role = ... # creator, participant
#     join_date = ... # data joined the discussion room/ topic
#     last_activity_date = models.DateTimeField(auto_now_add=True)
#     status = ... # active, muted, banned

#     def __str__(self):
#         return str(self.user)