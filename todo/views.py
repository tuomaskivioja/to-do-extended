from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.

def get_task_by_id(tasks,task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

@login_required(login_url='todo:login')
def index(request):
    task_form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    ctx = {"tasks": tasks, "form": task_form}
    return render(request, "todo/index.html", ctx)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index')) 
        else:
            return render(request, 'todo/login.html', {'error': 'Invalid login credentials'})
    
    return render(request, 'todo/login.html')

@login_required(login_url='login')  # Decorate the view with login_required to ensure only authenticated users can access it
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:login'))

def delete_task(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        task_id = body['taskId']
        task = Task.objects.get(id=int(task_id))
        task.delete()
        return HttpResponseRedirect(reverse('todo:index'))
    
    return HttpResponseRedirect(reverse('todo:index'))

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                user=request.user,
                name=form.cleaned_data['task'],
                description=form.cleaned_data['description'],
                priority=int(form.cleaned_data['priority'])
            )
            task.save()
    return HttpResponseRedirect(reverse('todo:index'))

@login_required
def task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    ctx = {"task": task}
    return render(request, "todo/task.html", ctx)

class AboutView(View):
    def get(self, request):
        return HttpResponse("this is about page")
