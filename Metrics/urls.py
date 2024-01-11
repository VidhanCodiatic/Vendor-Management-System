from django.urls import path
from Metrics.views import VendorHistoricalPerformanceView

urlpatterns = [
    path('historical_performance/', VendorHistoricalPerformanceView.as_view(),
        name='vendor-historical-performance'),
]