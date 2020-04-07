import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers import (
    AnonymousMetricsSerializer
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class AnonymousViewSet(ViewSet):
    """Actions that don't require auth"""

    @swagger_auto_schema(
        operation_id="SubmitAnonymousMetrics",
        method="POST",
        request_body=AnonymousMetricsSerializer(),
        responses={200: AnonymousMetricsSerializer()},
    )
    @action(methods=["POST"], detail=False)
    def submit_anonymous_metrics(self, request):
        """Called to submit the full anonymous metrics, expects to receive all answers for metric questions and the
        recordings."""
        ser = AnonymousMetricsSerializer(data=request.data, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)