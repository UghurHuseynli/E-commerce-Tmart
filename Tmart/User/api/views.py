from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from User.models import SubscriberUserModel, UserModel
from .serializers import RegisterSerializer, SubscriberSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

# class SubscriberView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         sub_serializer = SubscriberSerializer(data = request.data)
#         if sub_serializer.is_valid():
#             sub_serializer.save()
#             return Response(sub_serializer.data)
#         return Response(sub_serializer.errors)

class SubscriberView(CreateAPIView):
    queryset = SubscriberUserModel.objects.all()
    serializer_class = SubscriberSerializer

class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer