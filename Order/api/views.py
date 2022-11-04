from requests import request
from rest_framework.generics import ListCreateAPIView
from Order.models import CardItemModel
from .serializers import BasketSerializerGet, BasketSerializerCreate


class BasketApiView(ListCreateAPIView):
    queryset = CardItemModel.objects.all()
    serializer_class = BasketSerializerCreate

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasketSerializerGet
        else:
            return BasketSerializerCreate
