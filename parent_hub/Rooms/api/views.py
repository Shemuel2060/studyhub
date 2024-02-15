# import the serializers classes
from django.http import JsonResponse
from .serializers import RoomSerializer, PostSerializer, TopicSerializer
# decorators/annotations for function based views
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response

# import the models
from Rooms.models import Room, Topic, Post
from django.contrib.auth.models import User

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/api', # to this view
        'GET/api/rooms', # to all rooms
        'GET/api/room/:id', # to a single room
        'GET/api', # to the home for the api
        'GET/api/posts', # to all rooms
        'GET/api/post/:id', # to a single room
        'GET/api', # to the home for the api
        'GET/api/topics', # to all rooms
        'GET/api/topic/:id', # to a single room
        'GET/api', # to the home for the api
        'GET/api/users', # to all rooms
        'GET/api/user/:id', # to a single room
    ]
    
    return Response(routes)

@api_view(['GET','POST'])
def getRooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all() # get all rooms
        serializer = RoomSerializer(rooms, many=True) # serlialize them
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 


@api_view(['GET','POST'])
def getRoom(request, pk):
    if request.method == 'GET':
        room = Room.objects.get(pk=pk) # get single room 
        serializer = RoomSerializer(room, many=False) # serlialize single room
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 



@api_view(['GET','POST'])
def getTopics(request):
    if request.method == 'GET':
        topics = Topic.objects.all() # get all topics
        serializer = TopicSerializer(topics, many=True) # serlialize them
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 
    
    elif request.method=='POST':
        # create serializer from the posted data
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','POST'])
def getTopic(request, id):
    if request.method == 'GET':
        topic = Topic.objects.get(pk=id) # get single room 
        serializer = TopicSerializer(topic, many=False) # serlialize single room
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 



 
@api_view(['GET','POST'])
def getPosts(request):
    if request.method == 'GET':
        posts = Post.objects.all() # get all posts
        serializer = PostSerializer(posts, many=True) # serlialize them
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 

    elif request.method=='POST':
        # create serializer from the posted data
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','POST'])
def getPost(request, id):
    if request.method == 'GET':
        post = Post.objects.get(pk=id) # get single room 
        serializer = PostSerializer(post, many=False) # serlialize single room
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 



@api_view(['GET','POST'])
def getUsers(request):
    if request.method == 'GET':
        users = User.objects.all() # get all users
        serializer = PostSerializer(users, many=True) # serlialize them
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 

    elif request.method=='POST':
        # create serializer from the posted data
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','POST'])
def getUser(request, id):
    if request.method == 'GET':
        user = User.objects.get(pk=id) # get single room 
        serializer = PostSerializer(user, many=False) # serlialize single room
        
        data = serializer.data
        return Response(data) # instead of return JsonResponse(data, safe=False) 

