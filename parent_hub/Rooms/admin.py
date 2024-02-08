from django.contrib import admin
from .models import Room, Settings, Post, Topic, Participant


# Register your models here.

admin.site.register([Room,Settings,Post, Participant, Topic])