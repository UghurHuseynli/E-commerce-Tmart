from unicodedata import name
from django.urls import path
from .views import ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name = 'product'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name = 'product_detail'),
]