from django.urls import path

from Metrics.views import VendorPerformanceView

urlpatterns = [
    path('vendors/<int:vendor_id>/performance/',  VendorPerformanceView.as_view(), name='vendor-historical-performance'),
]