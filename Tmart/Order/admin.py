from django.contrib import admin
from .models import BillingAddressModel, CountryModel, PaymentDetailModel, CheckoutModel, WishlistModel, CardItemModel, CardModel
# Register your models here.

admin.site.register([BillingAddressModel, CountryModel, PaymentDetailModel, CheckoutModel, WishlistModel, CardItemModel, CardModel])