from django.db import models

# Create your models here.

class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)

