from django import forms
from .models import ReviewsModel

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewsModel
        fields = ['name', 'email', 'review', 'rate', 'img']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'placeholder': 'Type your name*'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'placeholder': 'Type your email*'
                }
            ),
            'review': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review*'
                }
            ),
            'rate': forms.TextInput(
                attrs={
                    'type': 'number',
                    'id': 'rateInputSection',
                    # 'readonly': 'readonly'
                }
            )
        }

        labels = {
            'img': 'Product image:',
        }
        