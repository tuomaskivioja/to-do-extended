from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm

# Create your views here.

def get_task_by_id(tasks,task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def index(request):
    task_form = TaskForm()
    if "tasks" not in request.session:
        request.session["tasks"] = []
    ctx = {"tasks": request.session["tasks"], "form": task_form }
    return render(request, "todo/index.html", ctx)

def add_task(request):
    request.session["hello"] = "world"
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = {
                "id": len(request.session["tasks"]) + 1,
                "name": form.cleaned_data['task'],
                "description": form.cleaned_data['description'],
                "priority": int(form.cleaned_data['priority']),
            }
            request.session["tasks"].append(task)
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    ctx = {"task": get_task_by_id(request.session['tasks'], id)}
    return render(request, "todo/task.html", ctx)

class AboutView(View):
    def get(self, request):
        return HttpResponse("this is about page")
