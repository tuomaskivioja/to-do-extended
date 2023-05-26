from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django import forms

# Create your views here.

tasks = [
    {"id": 1, "name": "Make video", "description": "make vid for course", "priority": 1},
    {"id": 2, "name": "Do dishes", "description": "wash dishes", "priority": 2},
    {"id": 3, "name": "Call mum", "description": "call mum fast!!!", "priority": 3}
]

def get_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def index(request):
    ctx = {"tasks": tasks }
    return render(request, "todo/index.html", ctx)

def add_task(request):
    print(request.POST)
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    ctx = {"task": get_task_by_id(id)}
    return render(request, "todo/task.html", ctx)

class AboutView(View):
    def get(self, request):
        return HttpResponse("this is about page")
