from django.contrib import admin
from .models import UserModel

# Register your models here.
admin.site.register(UserModel)

admin.site.site_header = 'Windwalker'
admin.site.site_title = 'My Admin'