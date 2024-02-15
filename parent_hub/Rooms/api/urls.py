
from django.urls import path

from . import views



urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('room/<str:pk>/', views.getRoom),
    path('topics',views.getTopics),
    path('topic/<str:id>/',views.getTopic),
    path('posts',views.getPosts),
    path('post/<str:id>/',views.getPost),
    
    path('users/', views.getUsers),
    path('user/<int:id>/', views.getUser)
]