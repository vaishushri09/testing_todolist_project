from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True   )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
