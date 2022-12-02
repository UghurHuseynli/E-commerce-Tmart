from django import template
from Product.models import CategoryModel


register = template.Library()

@register.filter
def check_has_child_menu(parent, categories):
    for category in categories:
        if category.parent_menu == parent:
            return True
    return False

@register.filter
def parent_category(categories, parent):
    result = []
    for category in categories:
        if category.parent_menu == parent:
            result.append(category)
    return result
