# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

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
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/edit_task.html', {'form': form, 'task': task})

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
        return redirect('todo_list')
@login_required
def mark_task_completed(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('todo_list')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
@login_required
def sleep_recommendation(request):
    if request.method == "POST":
        sleep_hours = int(request.POST.get("sleepHours"))
        work_hours = int(request.POST.get("workHours"))

        recommendation = ""
        work_recommendation = ""

        if sleep_hours >= 7 and work_hours <= 8:
            recommendation = "Great job! You're getting enough sleep and maintaining a balanced work schedule."
        elif sleep_hours < 7:
            recommendation = "Consider getting more sleep to stay refreshed and focused."
        elif work_hours > 8:
            recommendation = "You might want to consider taking short breaks or naps to prevent burnout."
        if work_hours < 5:
                work_recommendation = "Your work hours are quite low. Make sure to maintain a balanced work routine."
        elif work_hours > 10:
                work_recommendation = "Your work hours are high. Remember to take regular breaks and get enough rest."

        return render(request, "sleep.html", {"user_recommendation": recommendation, "work_recommendation": work_recommendation})

    return render(request, "sleep.html")