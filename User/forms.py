from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ValidationError
from.models import UserModel

class UserModelRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
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
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password*',
                    'type': 'password'
                }
            )
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError(message='Password must be at least 8 characters long')
        return password

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget= forms.TextInput(attrs={'placeholder': 'User Name*', 'type': 'text'}))
    password = forms.CharField(max_length = 30, widget= forms.PasswordInput(attrs={'placeholder': 'Password*'}))

class ForgetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Write your email', 'class': 'form-control', 'style': 'padding: 1.5rem 1rem 1.5rem 1rem'}))