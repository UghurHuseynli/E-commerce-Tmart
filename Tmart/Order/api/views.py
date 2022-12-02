from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from Order.models import CardItemModel, CardModel, WishlistModel
from .serializers import BasketSerializerGet, BasketSerializerCreate, WishlistSerializerGet, WishlistSerializerPost

class BasketApiViewset(ModelViewSet):
    queryset = CardItemModel.objects.all()
    serializer_class = BasketSerializerCreate
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasketSerializerGet
        else:
            return BasketSerializerCreate

    def list(self, request, *args, **kwargs):
        card = CardModel.objects.get(user = request.user)
        queryset = CardItemModel.objects.filter(card = card)
        serializer = BasketSerializerGet(queryset, many=True)
        return Response(serializer.data)


class WishlistViewset(ModelViewSet):
    queryset = WishlistModel.objects.all()
    serializer_class = WishlistSerializerGet
    permission_classes = []

    def create(self, request, *args, **kwargs):
        if WishlistModel.objects.filter(product_version = request.data.get('product_version')):
            return Response({'message': 'This object was already adding your wishlist'}, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WishlistSerializerGet
        else:
            return WishlistSerializerPost