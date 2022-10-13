from django.db import models
from User.models import UserModel
from Product.models import ProductVersionModel
# Create your models here.


class BillingAddressModel(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)
    message = models.TextField()
    company = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zip_code = models.CharField(max_length = 30)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.first_name

class CountryModel(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self) -> str:
        return self.name

class PaymentDetailModel(models.Model):
    card_name = models.CharField(max_length = 20)
    card_number = models.CharField(max_length = 20)
    card_date = models.DateTimeField()
    secure_code = models.CharField(max_length = 256)

    def __str__(self) -> str:
        return self.card_number

class CheckoutModel(models.Model):
    billing_id = models.ForeignKey(BillingAddressModel, on_delete = models.CASCADE)
    payment_id = models.ForeignKey(PaymentDetailModel, on_delete = models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user_id

class WishlistModel(models.Model):
    is_active = models.BooleanField()
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user_id

class CardModel(models.Model):
    at_buy = models.BooleanField()
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user_id
        
class CardItemModel(models.Model):
    quantity = models.IntegerField()
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete = models.CASCADE)
    card_id = models.ForeignKey(CardModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.card_id
