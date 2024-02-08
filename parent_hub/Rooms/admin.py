from django.contrib import admin
from .models import Rooms, Settings, Posts
# Register your models here.

admin.site.register([Rooms,Settings,Posts])