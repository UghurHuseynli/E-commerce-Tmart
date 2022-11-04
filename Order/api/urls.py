from django.urls import path
from .views import BasketApiView

urlpatterns = [
    path('card/', BasketApiView.as_view())
]