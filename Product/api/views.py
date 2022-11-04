from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from Product.models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer, ProductSerializerForGet

class ProductViewset(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializerForGet(queryset, many=True)
        return Response(serializer.data)

class CategoryViewset(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []