from django import forms
from django.forms import ValidationError
from .models import ContactModel

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'mail', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'type': 'text',
                    'name': 'name',
                    'placeholder': 'Your Name*'
                }
            ),
            'mail': forms.EmailInput(
                attrs= {
                    'type': 'email',
                    'name': 'email',
                    'placeholder': 'Mail*'
                }
            ),
            'subject': forms.TextInput(
                attrs= {
                    'type': 'text',
                    'name': 'subject',
                    'placeholder': 'Subject*'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'name': 'message',
                    'placeholder': 'Message*'
                }
            )
        }
