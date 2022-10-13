from unicodedata import name
from django.urls import path
from .views import customer_review, ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name = 'product'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name = 'product_detail'),
    path('review/', customer_review, name = 'customer_review')
]