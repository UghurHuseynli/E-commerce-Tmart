from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from User.models import SubscriberUserModel, UserModel


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberUserModel
        fields = ['email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.EmailField(
            required = True,
            validators = [UniqueValidator(queryset = UserModel.objects.all())]
        )
        model = UserModel
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
