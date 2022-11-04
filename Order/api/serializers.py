from requests import request
from rest_framework import serializers
from Order.models import CardItemModel, CardModel

class BasketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = CardItemModel
        fields = ['quantity', 'product_version']

    def create(self, validated_data):
        card, new_card = CardModel.objects.get_or_create(user = self.context['request'].user, at_buy = False)
        card_item = CardItemModel.objects.create(card = card, **validated_data)
        card_item.save()
        return card_item

class BasketSerializerGet(serializers.ModelSerializer):
    product_version = serializers.SerializerMethodField()

    def get_product_version(self, obj):
        return obj.product_version.name
    class Meta:
        model = CardItemModel
        fields = ['quantity', 'product_version']