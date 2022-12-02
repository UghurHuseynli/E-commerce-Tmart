from django import template
from Blog.models import BlogModel

register = template.Library()

@register.filter
def blog_category(category):
    return len(BlogModel.objects.filter(category = category))