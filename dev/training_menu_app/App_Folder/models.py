from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Workout(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,)
    response = models.TextField()

