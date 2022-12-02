from django import forms
from .models import CommentModel

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'comment_text']
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Name*',
                    'type': 'text'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'placeholder': 'Email*',
                    'type': 'email'
                }
            ),
            'comment_text': forms.Textarea(
                attrs = {
                    'placeholder': 'Message',
                    'type': 'text'
                }
            )
        }