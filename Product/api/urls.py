from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewset, CategoryViewset

router = DefaultRouter()
router.register(r'product', ProductViewset)
router.register(r'category', CategoryViewset)

urlpatterns = [
    path('', include(router.urls)), 
]