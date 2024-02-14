
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('',views.home, name='home'),
    # dynamic routing to rooms of topics clicked.
    path('room/<str:pk>/',views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    
    
    # path('create-room', views.createForm, name='create-room'),
    path('roomcreator', views.create_room, name='room-create'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
    
    
    path('edit-user', views.editUser, name='edit-user')
]