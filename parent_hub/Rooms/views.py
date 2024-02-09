from django.shortcuts import render, redirect
from .models import Topic, Room

from .forms import createRoomForm
# Create your views here.

def create_room(request):
    """for rendering the create room form."""
    form = createRoomForm(request.POST or None) # initialize the form
    if form.is_valid():
        form.save()
        form = createRoomForm() # to clear form fields
        return redirect('home') # after form submission, redirect to home page.
        
    context = {'form':form}
    return render(request,'Rooms/room_form.html', context)
    
def update_room(request, pk):
    """for updating the create room form."""
    # get room to update by its pk
    room = Room.objects.get(id=pk)
    # create an instance of that form attached to that room
    form = createRoomForm(instance=room) 
    if request.method == 'POST':
        # pre-populate form with data from that room
        form = createRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()            
            return redirect('home') # after form submission, redirect to home page.
        
    context = {'form':form}
    return render(request,'Rooms/room_form.html', context)

def deleteRoom(request, pk):
    """delete room"""
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete() # delete from db
        return redirect('home') # redirect to home page
    return render(request, 'Rooms/delete.html',{'obj':room})
    
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
    topics = Topic.objects.all() # query all topics from db
    context = {'allrooms':rooms, 'alltopics':topics}
    return render(request, 'Rooms/home.html', context)

# def createForm(request):
#     """create and update a room"""
#     context = {}
#     return render(request,'Rooms/room_form.html', context)