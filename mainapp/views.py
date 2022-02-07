from django.shortcuts import render
from django.http import  HttpResponse
from .models import Task

def index(req):
    tasks = Task.objects.all()
    return render(req, 'mainapp/index.html', {'title': 'main page of site', 'tasks': tasks})

def about(req):
    return render(req, 'mainapp/about.html')
