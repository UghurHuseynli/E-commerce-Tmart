from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect,render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
import random
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
from .models import UserModel
# from .token import TokenGenerator
from .forms import UserModelRegisterForm, UserLoginForm, ForgetForm
# Create your views here.
class LoginRegisterView(CreateView):
    model = UserModel
    template_name = 'login-register.html'
    form_class = UserModelRegisterForm

    def get(self, request, *args, **kwargs):
        context = {
            'form_register': UserModelRegisterForm(),
            'form_login': UserLoginForm()
        }
        return render(request, 'login-register.html', context = context)
    
    def post(self, request, *args, **kwargs):
        login_form = UserLoginForm()
        new_user = UserModelRegisterForm()
        if request.POST.get('email'):
            new_user = UserModelRegisterForm(request.POST)
            if new_user.is_valid():
                new_user.save()
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('login_register'))
        else:
            login_form = UserLoginForm(request.POST)
            user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or password incorrect')
        context = {
            'form_register': new_user,
            'form_login': login_form
        }
        return render(request, 'login-register.html', context=context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
        
class ForgetPasswordView(View):
    def get(self, request, *args, **kwargs):
        # context =  super().get(request, *args, **kwargs)
        context = {
            'forget_form': ForgetForm()
        }
        return render(request, 'forget_password.html', context=context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            # current_site = get_current_site(request)
            # mail_subject = 'Welcome to Tmart.'
            # message = render_to_string('acc_active_email.html', {
            #     'email': email,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            subject = 'Welcome to Tmart'
            a = random.randint(0, 1000000)
            message = f'Hi {email}, Please click the link below to reset your password.\nLink: http://127.0.0.1:8000/account/change-password/{a}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('/')

            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
            # email.send()
        context = {
            'forget_form': forget_form
        }
        return render(request, 'forget_password.html', context = context)

class ChangePasswordView(UpdateView):
    model = UserModel
    template_name = 'change_password.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'change_password.html', context={})