
from django.contrib import admin

from Metrics.models import HistoricalPerformance


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'vendor', 'date', 'on_time_delivery_rate',
        'quality_rating_avg', 'average_response_time',
        'fulfillment_rate',
    ]
