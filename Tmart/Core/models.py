from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class TeamModel(models.Model):
    team_member_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='team', default='../static/images/avatar/default_avatar.png', blank=True)
    facebook_url = models.CharField(max_length = 500)
    twitter_url = models.CharField(max_length = 500)
    instagram_url = models.CharField(max_length = 500)
    gmail_url = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.team_member_name

class ContactModel(models.Model):
    name = models.CharField(max_length = 30)
    mail = models.EmailField(max_length = 500)
    subject = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('contact')

class BlockedIp(models.Model):
    ip_addr = models.CharField(max_length = 15)

    def __str__(self):
        return self.ip_addr
