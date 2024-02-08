from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def room(request):
    """handle rooms"""
    return HttpResponse("<h1>Hello, Samuel</h1>")