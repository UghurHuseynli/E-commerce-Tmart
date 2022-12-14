from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CheckoutModel, CardItemModel, CardModel
from .forms import BillingAddressModelForm, PaymentDetailModelForm

# Create your views here.

class CheckoutView(LoginRequiredMixin, CreateView):
    model = CheckoutModel
    form_class = BillingAddressModelForm
    template_name = 'checkout.html'
    context_object_name = 'check'

    def get(self, request, *args, **kwargs):
        cardId = CardModel.objects.filter(user = request.user).first()
        price = 0
        for card in CardItemModel.objects.filter(card = cardId).all():
            price += card.quantity * card.product_version.price
        context = {
            'price': price,
            'billing': BillingAddressModelForm(),
            'payment': PaymentDetailModelForm()
        }
        return render(request, 'checkout.html', context=context)

    def post(self, request, *args, **kwargs):
        new_billing = BillingAddressModelForm(request.POST)
        new_payment = PaymentDetailModelForm(request.POST)
        if new_billing.is_valid() and new_payment.is_valid():
            new_billing.instance.user_id = request.user
            new_billing.save()
            new_payment.save()
            messages.success(request, 'Thank you for your payment. Your invoice has been sent to your mail.')
            return redirect('/')
        context = {
            'billing': new_billing,
            'payment': new_payment,
        }
        return render(request, 'checkout.html', context = context)


def cart(requests):
    return render(requests, 'cart.html')

def wishlist(reuqests):
    return render(reuqests, 'wishlist.html')