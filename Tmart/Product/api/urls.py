from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewset, CategoryViewset, ProductVersionViewset, ColorViewSet, SizeViewSet, TagsViewset, BrandViewset

router = DefaultRouter()
router.register(r'product', ProductViewset)
router.register(r'category', CategoryViewset)
router.register(r'product-versions', ProductVersionViewset)
router.register(r'product-colors', ColorViewSet)
router.register(r'product-sizes', SizeViewSet)
router.register(r'product-tags', TagsViewset)
router.register(r'product-brands', BrandViewset)

urlpatterns = [
    path('', include(router.urls)), 
]