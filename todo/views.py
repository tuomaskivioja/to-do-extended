from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm


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
    taskform = TaskForm()
    print(request.session['tasks'])
    if "tasks" not in request.session:
        request.session['tasks'] = []
    ctx = {"tasks": request.session['tasks'], "form": taskform }
    return render(request, "todo/index.html", ctx)

def add_task(request):
    print(request.POST)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task = {
                "id": len(tasks) + 1,
                "name": form.cleaned_data['task'],
                "description": form.cleaned_data['description'],
                "priority": int(form.cleaned_data['priority']),
            }
            request.session['tasks'].append(task)
            print(request.session['tasks'])
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    ctx = {"task": get_task_by_id(id)}
    return render(request, "todo/task.html", ctx)

class AboutView(View):
    def get(self, request):
        return HttpResponse("this is about page")
