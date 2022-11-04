from itertools import product
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from verify_email import verify_email
from .models import UserModel
from .forms import UserModelRegisterForm, UserLoginForm, ForgetForm, ResetForm
from .token import account_activation_token
from .tasks import send_email_task
# from .send_email import send_email

# Create your views here.

class ActivateUser(View):
    def get(self, request, *args, **kwargs):
        User = UserModel
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
            return redirect('login_register')
        else:
            messages.error(request, 'Activation link is invalid!')
        
        return redirect('/')

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
        if request.POST.get('form_register'):
            new_user = UserModelRegisterForm(request.POST)
            if new_user.is_valid():
                new_user_valid = new_user.save()
                new_user_valid.set_password(new_user_valid.password)
                new_user_valid.save()

                form_email = request.POST['email']
                mail_subject = 'Activate your user account.'
                message = render_to_string('password-activate.html', {
                        'user': new_user_valid,
                        'domain': get_current_site(request).domain,
                        'uid': urlsafe_base64_encode(force_bytes(new_user_valid.id)),
                        'token': account_activation_token.make_token(new_user_valid),
                        'protocol': 'https' if request.is_secure() else 'http'
                })
                # send_email(request, mail_subject, form_email)
                send_email_task.delay(mail_subject, message, form_email)
                messages.success(request, f'Dear {new_user_valid}, please go to you email {form_email} inbox and click on \
                                received activation link to confirm and complete the registration. Note: Check your spam folder.')
                return redirect('/')
        else:
            login_form = UserLoginForm(request.POST)
            user = authenticate(request, 
                                username = request.POST['username'], 
                                password = request.POST['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or password incorrect or your account not active')
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
        context = {
            'forget_form': ForgetForm()
        }
        return render(request, 'forget_password.html', context=context)

    def post(self, request, *args, **kwargs):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            if UserModel.objects.get(email = email):
                user = UserModel.objects.get(email = email)
                mail_subject = 'Reset your account password.'
                message = render_to_string('password-reset.html', {
                        'user': user,
                        'domain': get_current_site(request).domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                        'protocol': 'https' if request.is_secure() else 'http'
                })
                send_email_task.delay(mail_subject, message, email)
                messages.success(request, f'Dear {user}, please go to your email {email} inbox and click the received reset link to reset your password. Note: Check your spam folder.')
                return redirect('login_register')
            else:
                messages.error(request, f'The email you entered was not found')
        context = {
            'forget_form': forget_form
        }
        return render(request, 'forget_password.html', context = context)

class ChangePasswordView(UpdateView):
    def get(self, request, *args, **kwargs):
        User = UserModel
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            context = {
                'reset_form': ResetForm()
            }
            return render(request, 'change_password.html', context = context)
        else:
            messages.error(request, 'Activation link is invalid!')
        
        return redirect('/')
        
    def post(self, request, *args, **kwargs):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            User = UserModel
            uidb64 = kwargs['uidb64']
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
            user.set_password(request.POST['password'])
            user.save()
            messages.success(request, 'Your password successfully changed')
            return redirect('login_register')
        
        return render(request, 'change_password.html', context = {'reset_form': reset_form})