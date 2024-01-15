
from rest_framework import serializers

from Metrics.models import HistoricalPerformance


class HistoricalPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformance
        fields = [
            'id', 'vendor', 'date', 'on_time_delivery_rate',
            'quality_rating_avg', 'average_response_time',
            'fulfillment_rate',
        ]
        read_only_fields = ['id']