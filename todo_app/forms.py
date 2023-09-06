# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class TaskForm(forms.ModelForm):
    time_of_completion = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'time_of_completion']
       