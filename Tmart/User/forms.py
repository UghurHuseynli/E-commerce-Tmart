from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from verify_email import verify_email
from.models import UserModel

class UserModelRegisterForm(UserCreationForm):
    form_register = forms.CharField(widget = forms.TextInput(attrs={'value': 'register', 'type': 'hidden'}))
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'password1', 'form_register']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'placeholder': 'User Name*',
                    'type': 'text'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'Email*',
                }
            )
        }

    def clean(self):
        if not verify_email(self.cleaned_data['email']):
            self.add_error('email', 'Please enter a valid email address')
        return super(UserModelRegisterForm, self).clean()

    def __init__(self, *args, **kwargs):
        super(UserModelRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {
            'placeholder': 'Password*',
            'type': 'password'
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': 'Password Confirm*',
            'type': 'password'
        }
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget= forms.TextInput(attrs={'placeholder': 'User Name*', 'type': 'text'}))
    password = forms.CharField(max_length = 30, widget= forms.PasswordInput(attrs={'placeholder': 'Password*'}))

class ForgetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Write your email', 'class': 'form-control', 'style': 'padding: 1.5rem 1rem 1.5rem 1rem'}))

class ResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'New Password', 'class': 'form-control', 'style': 'padding: 1.5rem 1rem 1.5rem 1rem'}))

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            if len(password) == 0:
                return ValidationError('This field is required.')
            else:
                return ValidationError('Your password must be at least 8 characters.')
        
        else: return password