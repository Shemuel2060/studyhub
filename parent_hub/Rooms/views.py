from django.shortcuts import render
from .models import Topic, Room

# Create your views here.

def room(request, pk):
    """handle rooms"""
    
    rooms = Room.objects.all()
    allrooms = {'allrooms':rooms}
    for aroom in allrooms['allrooms']:
        if aroom.id == int(pk):
            context = {'room':aroom}
            break
        else:
            context={'room':'Welcome to Rooms'}
        
    return render(request, 'Rooms/room.html',context)

def home(request):
    """home - the main app interface"""
    # render out topics as links to pages for each topic
    rooms = Room.objects.all() # query all topics from db
    context = {'allrooms':rooms}
    return render(request, 'Rooms/home.html', context)

def createForm(request):
    """create and update a room"""
    context = {}
    return render(request,'Rooms/room_form.html', context)