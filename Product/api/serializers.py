from rest_framework import serializers
from Product.models import ProductModel, CategoryModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'rating', 'detail_description', 'img', 'category_id']

class ProductSerializerForGet(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category_id')

    def get_category_id(self, obj):
        return obj.category_id.category_name

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price', 'rating', 'detail_description', 'img', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'category_name', 'parent_menu', 'is_navbar', 'icons']