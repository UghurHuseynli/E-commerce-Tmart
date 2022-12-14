from django.urls import path
from .views import LoginRegisterView, LogoutView, ForgetPasswordView, ChangePasswordView, ActivateUser

urlpatterns = [
    path('', LoginRegisterView.as_view(), name='login_register'),
    path('password-reset/', ForgetPasswordView.as_view(), name='password_reset'),
    path('change-password/<uidb64>/<token>/', ChangePasswordView.as_view(), name= 'change_password'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('activate/<uidb64>/<token>', ActivateUser.as_view(), name='activate'),

]