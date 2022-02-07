from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(req):
    tasks = Task.objects.all()
    return render(req, 'mainapp/index.html', {'title': 'main page of site', 'tasks': tasks})


def about(req):
    return render(req, 'mainapp/about.html')

def create(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    context = {
        'form': form
    }
    return render(req, 'mainapp/create.html', context)
