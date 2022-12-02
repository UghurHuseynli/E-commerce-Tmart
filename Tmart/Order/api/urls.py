from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasketApiViewset, WishlistViewset

router = DefaultRouter()
router.register(r'card', BasketApiViewset)
router.register(r'wishlist', WishlistViewset)

urlpatterns = [
    path('', include(router.urls))
]