from django.contrib import admin
from .models import TeamModel, ContactModel, BlockedIp

# Register your models here.

admin.site.register([TeamModel, ContactModel, BlockedIp])