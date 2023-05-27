from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm
from .models import Task

# Create your views here.

def get_task_by_id(tasks,task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def index(request):
    task_form = TaskForm()
    tasks = Task.objects.all()
    ctx = {"tasks": tasks, "form": task_form}
    return render(request, "todo/index.html", ctx)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                name=form.cleaned_data['task'],
                description=form.cleaned_data['description'],
                priority=int(form.cleaned_data['priority'])
            )
            task.save()
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    task = Task.objects.get(id=id)
    ctx = {"task": task}
    return render(request, "todo/task.html", ctx)

class AboutView(View):
    def get(self, request):
        return HttpResponse("this is about page")
