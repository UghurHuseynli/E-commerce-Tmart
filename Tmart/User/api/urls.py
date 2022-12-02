from django.urls import path
from .views import SubscriberView, MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('subscribe/', SubscriberView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]