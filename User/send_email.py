from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import UserModel
from .forms import UserModelRegisterForm, UserLoginForm, ForgetForm, ResetForm
from .token import account_activation_token
from .tasks import send_email_task



def send_email(request, subject, email):
    user = request.user
    message = render_to_string('password-activate.html', {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    send_email_task.delay(subject, message, email)