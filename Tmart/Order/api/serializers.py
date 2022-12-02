from rest_framework import serializers
from Order.models import CardItemModel, CardModel, WishlistModel

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
    product_version_name = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_url(self, obj):
        return f'{obj.product_version.get_absolute_url()}'

    def get_price(self, obj):
        price = obj.product_version.price
        if obj.product_version.discount:
            if obj.product_version.is_percent:
                return price - price * obj.product_version.discount / 100
            else:
                return price - obj.product_version.discount
        return price

    def get_product_version_name(self, obj):
        return obj.product_version.product.name

    def get_image(self, obj):
        return f'{obj.product_version.product.img.url}'

    def get_color(self, obj):
        return [color.color for color in obj.product_version.color.all()]
    
    def get_size(self, obj):
        return [size.size for size in obj.product_version.size.all()]
    class Meta:
        model = CardItemModel
        fields = ['id', 'quantity', 'product_version', 'product_version_name', 'color', 'size', 'image', 'price', 'url']

class WishlistSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = ['product_version']
    
    def create(self, validated_data):
        wishlist = WishlistModel.objects.create(is_active=False, user = self.context['request'].user, **validated_data)
        wishlist.save()
        return wishlist

class WishlistSerializerGet(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    is_stock = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        return obj.product_version.product.name
    
    def get_image(self, obj):
        return f'{ obj.product_version.product.img.url }'
    
    def get_is_stock(self, obj):
        return obj.product_version.is_stock

    def get_url(self, obj):
        return f'{obj.product_version.get_absolute_url()}'
    
    def get_price(self, obj):
        return obj.product_version.price

    class Meta:
        model = WishlistModel
        fields = ['id', 'product_name', 'product_version', 'image', 'is_stock', 'url', 'price']
