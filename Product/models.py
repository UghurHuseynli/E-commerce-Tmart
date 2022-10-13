from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse_lazy
# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length = 100)
    parent_menu = models.ForeignKey('CategoryModel', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category_name

class ProductModel(models.Model):
    name = models.CharField(max_length = 300)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    detail_description = models.TextField()
    price = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to='product_cover')
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductModel, self).save(*args, **kwargs)

class ProductVersionModel(models.Model):
    price = models.FloatField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product_id}'
    
    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'slug': self.product_id__slug})

class ProductImgModel(models.Model):
    img = models.ImageField(upload_to=f'products/')
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product_version_id}'

class ProductColorModel(models.Model):
    color = models.CharField(max_length = 20)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.color

class ProductSizeModel(models.Model):
    size = models.CharField(max_length = 5)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.size

class FeaturesModel(models.Model):
    feature = models.TextField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.feature

class DataSheetModel(models.Model):
    data = models.TextField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.data

class ReviewsModel(models.Model):
    name = models.CharField(max_length = 30)
    review = models.TextField()
    email = models.EmailField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='reviews/')
    rate = models.FloatField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
