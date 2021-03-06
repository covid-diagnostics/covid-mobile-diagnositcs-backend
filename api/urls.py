"""Urls for API prefixed by api/."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter, Route, escape_curly_brackets

from api.views import (
    MeViewSet,
    QuestionViewSet,
    MeasurementViewSet,
    PPGMeasurementViewSet,
    QuestionResponseViewSet,
    VoiceRecordingViewSet,
    UserInfoViewSet,
)


class HyphenatedRouter(DefaultRouter):
    """Same as Default Router only switches _ with -"""

    def _get_dynamic_route(self, route, action):
        initkwargs = route.initkwargs.copy()
        initkwargs.update(action.kwargs)

        url_path = escape_curly_brackets(action.url_path)

        return Route(
            url=route.url.replace("{url_path}", url_path.replace("_", "-")),
            mapping=action.mapping,
            name=route.name.replace("{url_name}", action.url_name),
            detail=route.detail,
            initkwargs=initkwargs,
        )


router = HyphenatedRouter()  # pylint: disable=invalid-name
router.register(r"me", MeViewSet, basename="me")
router.register(r"question", QuestionViewSet, basename="question")
router.register(
    r"question-response", QuestionResponseViewSet, basename="question-response"
)
router.register(r"measurement", MeasurementViewSet, basename="measurement")
router.register(r"ppg-measurement", PPGMeasurementViewSet, basename="ppg-measurement")
router.register(r"voice-recording", VoiceRecordingViewSet, basename="voice-recording")
router.register(r"user-info", UserInfoViewSet, basename="user-info")

urlpatterns = [] + router.urls
