from django.shortcuts import render, redirect
from django.db.models import Q # look up queries
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required # restrict access and permissions
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Room, Post
from .forms import createRoomForm
# Create your views here.

@login_required(login_url='login') # if not logged in, can't create room, redirect to login
def create_room(request):
    """for rendering the create room form."""
    form = createRoomForm(request.POST or None) # initialize the form
    if form.is_valid():
        room = form.save(commit=False) # get room before committing to db
        room.host = request.user # host is the logged in user creating the room
        form.save() # saave form with committing to db
        form = createRoomForm() # to clear form fields
        return redirect('home') # after form submission, redirect to home page.
        
    context = {'form':form}
    return render(request,'Rooms/room_form.html', context)


@login_required(login_url='login') # if not logged in, can't update room, redirect to login
def update_room(request, pk):
    """for updating the create room form."""
    # get room to update by its pk
    room = Room.objects.get(id=pk)
    # create an instance of that form attached to that room
    
    # restrict non owner from updating a room
    if request.user != room.host:
        return HttpResponse('You CANNOT delete since you are not the owner')
    
    form = createRoomForm(instance=room) 
    if request.method == 'POST':
        # pre-populate form with data from that room
        form = createRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()            
            return redirect('home') # after form submission, redirect to home page.
        
    context = {'form':form}
    return render(request,'Rooms/room_form.html', context)

@login_required(login_url='login') # if not logged in, can't delete room, redirect to login
def deleteRoom(request, pk):
    """delete room"""
    room = Room.objects.get(id=pk)
    
    # restrict non owner from deleting a room
    if request.user != room.host:
        return HttpResponse('You CANNOT delete since you are not the owner')
    
    
    if request.method == 'POST':
        room.delete() # delete from db
        return redirect('home') # redirect to home page
    return render(request, 'Rooms/delete.html',{'obj':room})
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all() # get all rooms user is in
    posts = user.post_set.all() # get all posts for this user
    topics = Topic.objects.all() # get all topics 
    topiccount = topics.count() # total topics
    context={'participant':user, 'allrooms':rooms, 
             'alltopics':topics, 'topiccount':topiccount, 'posts':posts}
    return render(request, 'Rooms/profile.html', context)
    
def room(request, pk):
    """handle rooms"""
    # APPROACH 1: Till able to post comments in a room - working with the single room
    roomy = Room.objects.get(id=pk) # get this room
    participants = roomy.participants.all() # get all participants
    
    # get posts in a room
    room_posts = roomy.post_set.all().order_by('-created_on') # or
    # room_posts = Post.objects.filter(room_id=pk).order_by('-created_on') 
    
    # create new posts from typed posts in the chat room
    if request.method == 'POST':
        new_post = Post.objects.create(
            author = request.user,
            room = roomy,
            body = request.POST.get('body')
        )
        roomy.participants.add(request.user) # add logged in user who has posted to the conversation
        return redirect('room', pk=new_post.room.id) # imitate a page refresh.
    
    context = {'room':roomy, 'room_posts':room_posts, 'participants':participants}
    
    # APPROACH 2: Till able to post comments in a room- Picking single room from all rooms
    
    # rooms = Room.objects.all()
    # allrooms = {'allrooms':rooms}
    # # get messages in a room and order them in last posted
    # # room_posts = room.post_set.all() # get all messages in a given room
    #  # get posts for this room
    # room_posts = Post.objects.filter(room_id=pk).order_by('-created_on') 
    
    
    # if request.method == 'POST':
    #     new_post = Post.objects.create(
    #         author = request.user,
    #         room = Room.objects.get(id=pk),
    #         body = request.POST.get('body')
    #     )
    #     return redirect('room', pk=new_post.room.id) # imitate a page refresh.
    
    # getting specific room from all rooms.
    # for aroom in allrooms['allrooms']:
    #     room_id = aroom.id
    #     if room_id == int(pk):
    #         context = {'room':aroom, 'room_posts':room_posts}
    #         break
    #     else:
    #         context={'room':'Welcome to Rooms'}
        
    return render(request, 'Rooms/room.html',context)

@login_required(login_url='login') # if not logged in, can't delete post, redirect to login
def deletePost(request, pk):
    """delete post created by user."""
    post = Post.objects.get(id=pk) # get the post.
    
    # restrict non owner from deleting a room
    if request.user != post.author:
        return HttpResponse('You CANNOT delete since you are not the owner')
      
    if request.method == 'POST':
        post.delete() # delete from db
        return redirect('home') # redirect to home page (better to go to room)
    return render(request, 'Rooms/delete.html',{'obj':post})

def loginPage(request):
    """login page..."""
    page = 'login' # used to determine if to render login page or register page.
    # prevent re-logging in
    if request.user.is_authenticated:
        return redirect('home')
    
    # confirm a post method
    if request.method == 'POST':
        # get entered data
        name = request.POST.get('username').lower()
        pw = request.POST.get('password')
        
        # confirm user exists in the db
        try:
            user = User.objects.get(username=name)
        except:
            messages.error(request, 'User does not exist')
        # user confirmed to exist, auntheticate
        user = authenticate(username=name,password=pw) # returns user obj or None
        if user is not None: # if user != None:
            # log the user in
            login(request, user)
            return redirect('home') # redirect to home page
        else:
            messages.error(request,'username or password does not exist')
            
    context = {'page':page}
    return render(request, 'Rooms/login_register.html', context)

def registerPage(request):
    # initialize the registration form to be seen when empty
    form = UserCreationForm()
    if request.method == 'POST':
        # pass the data to the form
        form = UserCreationForm(request.POST)
        # check if form is valid
        if form.is_valid():
            # save form without committing it, clean user data
            user = form.save(commit=False)
            user.username = user.username.lower()
            # save and commit user 
            user.save() 
            # log the user in
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong!')
            
    context = {'form':form}
    return render(request, 'Rooms/login_register.html', context)
    
def logoutUser(request): # does not need a template
    """log user out.."""
    logout(request) # deletes all user info if logged in
    return redirect('home')
    
def home(request):
    """home - the main app interface"""
    topics = Topic.objects.all() # query all topics from db
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    # if request.GET.get('q')!=None:
    #     q=request.GET.get('q')
    # else:
    #     '' # fails for the home url... localhost:8000 just. WHY?
    # get only rooms with searched topic names.
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) | # room name
        Q(description__icontains = q) # room description
    )
    posts = Post.objects.all().filter(Q(room__topic__name__icontains=q)) # get all posts.. can filter here
    roomcount = rooms.count() # get total rooms
    topiccount = topics.count() # get total topics
    context = {
        'allrooms':rooms, 
        'alltopics':topics, 
        'roomcount':roomcount,
        'topiccount':topiccount,
        'posts':posts}
    return render(request, 'Rooms/home.html', context)

# def createForm(request):
#     """create and update a room"""
#     context = {}
#     return render(request,'Rooms/room_form.html', context)