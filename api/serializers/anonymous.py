from rest_framework import serializers

from api.models import AnonymousMetrics


class AnonymousMetricsSerializer(serializers.ModelSerializer):
    """(De)Serialize a submitted anonymous examples that contains all of the metrics, and recordings.."""

    class Meta:
        model = AnonymousMetrics