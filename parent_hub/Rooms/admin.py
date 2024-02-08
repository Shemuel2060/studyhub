from django.contrib import admin
from .models import Room,Post,Topic


# Register your models here.

admin.site.register([Room,Post, Topic])