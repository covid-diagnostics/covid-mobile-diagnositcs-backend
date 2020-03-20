from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenViewBase

from api.serializers import UserSerializer, UserTokenSerializer


class TokenObtainUserSerializer(TokenObtainPairSerializer):
    """Returns the refersh and access token as well as the user"""

    def validate(self, attrs):
        data = super().validate(attrs)
        data["token"] = {"access": data["access"], "refresh": data["refresh"]}
        del data["access"]
        del data["refresh"]
        data["user"] = UserSerializer(self.user).data
        return data


@method_decorator(
    swagger_auto_schema(
        operation_id="manualLogin", responses={200: UserTokenSerializer()}
    ),
    "post",
)
class TokenObtainUserView(TokenViewBase):

    serializer_class = TokenObtainUserSerializer
