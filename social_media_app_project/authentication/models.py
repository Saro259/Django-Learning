from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model() # Using in-built user model to get the user model from the particula function
