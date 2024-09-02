from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


from todoapp.models import Task 


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    login_url = reverse_lazy('login')

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = "task"
    login_url = reverse_lazy('login')


class TaskListLoginView(LoginView):
    fields = '__all__'
    template_name = 'todoapp/login.html'
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('tasks')
