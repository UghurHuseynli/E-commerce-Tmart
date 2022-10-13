from django.urls import path
from .views import BlogView, BlogDetailsView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('detail/<slug:slug>', BlogDetailsView.as_view(), name='blog_details')
]