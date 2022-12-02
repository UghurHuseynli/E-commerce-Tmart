from rest_framework import serializers
from Product.models import ProductModel, CategoryModel, ProductVersionModel, ProductImgModel, ProductColorModel, ProductSizeModel, TagsModel, BrandModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'rating', 'detail_description', 'img', 'category', 'brand', 'tag',]

class ProductSerializerForGet(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    url = serializers.SerializerMethodField()
    new_price = serializers.SerializerMethodField()

    def get_new_price(self, obj):
        min_price = min([(product.price, product.id) for product in ProductVersionModel.objects.filter(product = obj)])
        product = ProductVersionModel.objects.get(id = min_price[1])
        if product.discount:
            if product.is_percent:
                return product.price - (product.price * product.discount / 100)
            else:
                return product.price - product.discount
        return product.price

    def get_url(self, obj):
        return f'{ obj.get_absolute_url() }'

    def get_category(self, obj):
        return obj.category.category_name

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price', 'rating', 'detail_description', 'img', 'category', 'url', 'new_price', 'brand', 'tag',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'category_name', 'parent_menu', 'is_navbar', 'icons']

class ProductVersionSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_colors(self, obj):
        return [color.color for color in obj.color.all()]
    
    def get_sizes(self, obj):
        return [size.size for size in obj.size.all()]

    def get_images(self, obj):
        return [image.img.url for image in ProductImgModel.objects.filter(product_version = obj)]

    class Meta:
        model = ProductVersionModel
        fields = ['id', 'price', 'colors', 'sizes', 'images', 'discount', 'is_percent', 'is_stock', 'product', 'stock_size']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorModel
        fields = ['id', 'color']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizeModel
        fields = ['id', 'size']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = ['id', 'name']
    
class BrandSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return f'{obj.img.url}'
    class Meta:
        model = BrandModel
        fields = ['id', 'name', 'image']

