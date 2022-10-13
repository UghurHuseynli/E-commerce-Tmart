from django.shortcuts import render
from django.views.generic import CreateView
from .models import CheckoutModel
from .forms import BillingAddressModelForm, PaymentDetailModelForm

# Create your views here.

def cart(requests):
    return render(requests, 'cart.html')

class CheckoutView(CreateView):
    model = CheckoutModel
    form_class = BillingAddressModelForm
    template_name = 'checkout.html'
    context_object_name = 'check'

    def get(self, request, *args, **kwargs):
        context = {
            'billing': BillingAddressModelForm(),
            'payment': PaymentDetailModelForm()
        }
        return render(request, 'checkout.html', context=context)

def checkout(requests):
    return render(requests, 'checkout.html')

def cart(requests):
    return render(requests, 'cart.html')

def wishlist(reuqests):
    return render(reuqests, 'wishlist.html')