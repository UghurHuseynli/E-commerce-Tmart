from modeltranslation.translator import translator, TranslationOptions
from .models import ProductModel

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'detail_description')

translator.register(ProductModel, ProductTranslationOptions)