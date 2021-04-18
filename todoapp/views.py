from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
from django.shortcuts import render


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklist')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklist')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasklist')


def filter_form(request):
    form = TaskForm()
    return render(request, 'todoapp/filter_form.html', {'form': form})


def filter_task(request):
    priority = ''

    form = TaskForm(request.POST)
    if form.is_valid():
        priority = form.cleaned_data.get("priority")

    tasks = Task.objects.filter(priority=priority)

    return render(request, 'todoapp/filter_task.html', {'tasks': tasks})
