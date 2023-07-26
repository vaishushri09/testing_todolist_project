from django.shortcuts import render, redirect

from .models import Task
def test_view(request):
    return render(request,'todo_app/add_task.html')

def todo_list(request):
    tasks = Task.objects.all()
    print(tasks[0])
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo_app/add_task.html')

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed')
        task.title = title
        task.description = description
        task.completed = bool(completed)
        task.save()
        return redirect('todo_list')
    return render(request, 'todo_app/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete_task.html', {'task': task})
# Create your views here.
from django.http import HttpResponse

