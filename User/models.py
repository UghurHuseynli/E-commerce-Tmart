from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

# Create your models here.

class UserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default='../static/images/avatar/default_avatar.png', blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('login_register')