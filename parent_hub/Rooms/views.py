from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def room(request):
    """handle rooms"""
    return render(request, 'Rooms/room.html',{})

def home(request):
    """home - the main app interface"""
    return render(request, 'Rooms/home.html', {})