
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # dynamic routing to rooms of topics clicked.
    path('room/<str:pk>/',views.room, name='room'),
    
    
    # path('create-room', views.createForm, name='create-room'),
    path('roomcreator', views.create_room, name='room-create')
]