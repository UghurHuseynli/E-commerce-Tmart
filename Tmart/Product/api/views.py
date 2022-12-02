from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from Product.models import CategoryModel, ProductModel, ProductVersionModel, ProductColorModel, ProductSizeModel, TagsModel, BrandModel
from .serializers import CategorySerializer, ProductSerializer, ProductSerializerForGet, ProductVersionSerializer, ColorSerializer, SizeSerializer, TagsSerializer, BrandSerializer

class ProductViewset(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializerForGet
    permission_classes = []

    def get_queryset(self):
        queryset = super(ProductViewset, self).get_queryset()

        category = self.request.GET.get('category')
        sort = self.request.GET.get('sort')
        size = self.request.GET.get('size')
        tag = self.request.GET.get('tag')
        price = self.request.GET.get('price')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')

        if category:
            subcategories = CategoryModel.objects.filter(parent_menu = category).all()
            if subcategories:
                ids = [category.id for category in subcategories]
                queryset = ProductModel.objects.filter(category__in = ids).all()
            else:
                queryset = ProductModel.objects.filter(category = category)

        if sort:
            if sort == 'max':
                queryset = queryset.order_by('-price')

            elif sort == 'min':
                queryset = queryset.order_by('price')
            
            elif sort == 'name':
                queryset = queryset.order_by('name')
            
            elif sort == 'name-reverse':
                queryset = queryset.order_by('-name')

        if size:
            result = []
            [result.append(product_version.product) for product_version in ProductVersionModel.objects.filter(Q(product__in = queryset) & Q(size = size)).all() if product_version.product not in result]
            queryset = result

        if tag:
            l = []
            for query in queryset:
                for t in query.tag.all():
                    if t.id == int(tag):
                        l.append(query)
            queryset = l

        if brand:
            queryset = [query for query in queryset if query.brand.id == int(brand)]

        if color:
            result = []
            [result.append(product_version.product) for product_version in ProductVersionModel.objects.filter(Q(product__in = queryset) & Q(color = color)).all() if product_version.product not in result]
            queryset = result

        if price:
            product_ids = [query.id for query in queryset]
            if price == '0-50':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=0) & Q(price__lte=50)))

            elif price == '50-100':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=50) & Q(price__lte=100)))
            
            elif price == '100-500':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=100) & Q(price__lte=500)))
            
            elif price == '500-1000':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=500) & Q(price__lte=1000)))
            
            elif price == '1000-2000':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=1000) & Q(price__lte=2000)))

            elif price == '2000-5000':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=2000) & Q(price__lte=5000)))
            
            elif price == '5000-':
                queryset = (ProductModel.objects.filter(Q(id__in = product_ids) & Q(price__gt=5000)))

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializerForGet
        else: 
            return ProductSerializer

class CategoryViewset(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class ProductVersionViewset(ModelViewSet):
    queryset = ProductVersionModel.objects.all()
    serializer_class = ProductVersionSerializer
    permission_classes = []
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']

class ColorViewSet(ModelViewSet):
    queryset = ProductColorModel.objects.all()
    serializer_class = ColorSerializer
    permission_classes = []

class SizeViewSet(ModelViewSet):
    queryset = ProductSizeModel.objects.all()
    serializer_class = SizeSerializer
    permission_classes = []

class TagsViewset(ModelViewSet):
    queryset = TagsModel.objects.all()
    serializer_class = TagsSerializer
    permission_classes = []

class BrandViewset(ModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer
    permission_classes = []

