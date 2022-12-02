from django.contrib import admin
from .models import BlogModel, CommentModel

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title',]}

admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register([CommentModel])