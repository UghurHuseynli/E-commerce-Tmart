from django.contrib import admin
from .models import UserModel, SubscriberUserModel

# Register your models here.
admin.site.register([UserModel, SubscriberUserModel])