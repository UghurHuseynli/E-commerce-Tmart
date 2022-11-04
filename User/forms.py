from django import forms
from django.forms import ValidationError
from.models import UserModel

class UserModelRegisterForm(forms.ModelForm):
    form_register = forms.CharField(widget = forms.TextInput(attrs={'value': 'register', 'type': 'hidden'}))
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'form_register']
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

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 2:
            if len(username) == 0:
                return ValidationError('This field is required.')
            else:
                return ValidationError('Your username must be at least 2 characters.') 
        
        elif UserModel.objects.filter(username = username).exists():
            return ValidationError('This username already used, please select another username.')

        else: return username   

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            if len(password) == 0:
                return ValidationError('This field is required.')
            else:
                return ValidationError('Your password must be at least 8 characters.') 
        elif password in self.cleaned_data['username']:
            return ValidationError('Your password is similar to your username, please enter a secure password ')
        
        else: return password
        
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