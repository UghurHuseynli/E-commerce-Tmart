from django.urls import path
from .views import cart, wishlist, CheckoutView

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('wishlist/', wishlist, name='wishlist')
]