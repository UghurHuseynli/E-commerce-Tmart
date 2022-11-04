from django import forms
from .models import BillingAddressModel, PaymentDetailModel, CountryModel

class BillingAddressModelForm(forms.ModelForm):
	countries = [(country_1.name, country_2.name) for country_1, country_2 in zip(CountryModel.objects.all(), CountryModel.objects.all())]
	country = forms.ChoiceField(choices=countries)
	class Meta:
		model = BillingAddressModel
		fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'company', 'country',  'state', 'zip_code']

		widgets = {
			'first_name': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'First Name*'
				}
			),
			'last_name': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Last Name*'
				}
			),
			'email': forms.EmailInput(
				attrs= {
					'type': 'email',
					'placeholder': 'Email*'
				}
			),
			'phone': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Phone*'
				}
			),
			'message': forms.Textarea(
				attrs= {
					'name': 'message',
					'placeholder': 'Message*'
				}
			),
			'company': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Company Name*'
				}
			),
			'state': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'State*'
				}
			),
			'zip_code': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Zip Code*'
				}
			),
		}

class PaymentDetailModelForm(forms.ModelForm):

	class Meta:
		model = PaymentDetailModel
		fields = ['card_name', 'card_number', 'card_date', 'secure_code']

		widgets = {
			'card_name': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Name on Card*'
				}
			),
			'card_number': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Card Number*'
				}
			),
			# 'card_date': DatePickerInput(),
			'card_date': forms.DateInput(
				attrs={
					'type': 'date'
				}
			),

			'secure_code': forms.TextInput(
				attrs= {
					'type': 'text',
					'placeholder': 'Secure Code*'
				}
			),
		}