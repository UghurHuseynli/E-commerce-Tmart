from django.contrib import admin
from .models import CategoryModel, ProductModel, ProductVersionModel, ProductImgModel, ProductSizeModel, ProductColorModel, FeaturesModel, DataSheetModel, ReviewsModel, BrandModel, TagsModel
from modeltranslation.admin import TranslationAdmin


# Register your models here.
class ProductModelAdmin(TranslationAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register([CategoryModel, BrandModel, ProductVersionModel, ProductImgModel, ProductColorModel, ProductSizeModel, FeaturesModel, DataSheetModel, ReviewsModel, TagsModel])