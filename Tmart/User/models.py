from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

# Create your models here.

class UserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default='../static/images/avatar/default_avatar.png', blank=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique = True)
    is_active = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('login_register')

class SubscriberUserModel(models.Model):
    email = models.EmailField(unique = True)

    def __str__(self) -> str:
        return self.email


