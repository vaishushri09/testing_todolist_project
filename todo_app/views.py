# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from .models import Task
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'todo_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'todo_app/login.html'

@login_required
def todo_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description, user=request.user)
        return redirect('todo_list')
    return render(request, 'todo_app/add_task.html')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
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

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete_task.html', {'task': task})
@login_required
def test_view(request):
    return render(request,'todo_app/add_task.html')

@login_required
def all_user_tasks(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
        return render(request, 'todo_app/all_user_tasks.html', {'tasks': tasks})
    else:
        return redirect('')
