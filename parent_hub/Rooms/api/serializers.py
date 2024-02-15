# import serializers 
from rest_framework import serializers


# import the models to work serialize

from Rooms.models import Room, Topic, Post

from django.contrib.auth.models import User


# create serializer classes for each model


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude=['password']


