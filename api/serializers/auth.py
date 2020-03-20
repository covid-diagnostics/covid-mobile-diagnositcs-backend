from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .user import UserSerializer


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class UserTokenSerializer(serializers.Serializer):
    user = UserSerializer(source="*", read_only=True)

    token = serializers.SerializerMethodField(read_only=True)

    @swagger_serializer_method(TokenSerializer())
    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        ser = TokenSerializer(
            data={"refresh": str(refresh), "access": str(refresh.access_token)}
        )
        ser.is_valid()
        return ser.data

    @swagger_serializer_method(UserSerializer(read_only=True))
    def get_user(self, obj):
        return UserSerializer(obj).data
