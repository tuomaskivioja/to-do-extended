from django.urls import path
from .views import index, AboutView, task, add_task

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutView.as_view(), name="about"),
    path('task/<int:id>', task, name="task"),
    path('add_task', add_task, name='add_task')
]
