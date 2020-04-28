from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenViewBase

from api.serializers import UserSerializer, UserTokenSerializer, TokenObtainUserSerializer


@method_decorator(
    swagger_auto_schema(
        operation_id="manualLogin", responses={200: UserTokenSerializer()}
    ),
    "post",
)
class TokenObtainUserView(TokenViewBase):

    serializer_class = TokenObtainUserSerializer
