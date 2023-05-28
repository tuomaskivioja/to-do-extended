from django.urls import path
from .views import index, AboutView, task, add_task, login_user, logout_user, delete_task, register_user

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutView.as_view(), name="about"),
    path('task/<int:id>', task, name="task"),
    path('add_task', add_task, name='add_task'),
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_task/', delete_task, name='delete'),
    path('register/', register_user, name='register'),
]
