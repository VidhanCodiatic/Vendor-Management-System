

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from Vendors.models import Vendor

from Metrics.models import HistoricalPerformance
from Metrics.permissions import PurchaseOrderPermission
from Metrics.serializers import HistoricalPerformanceSerializer


class VendorPerformanceView(APIView):
    permission_classes = [PurchaseOrderPermission]
    
    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, id=vendor_id)
        performance_data = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = HistoricalPerformanceSerializer(performance_data, many=True)

        return Response({
            'vendor_id': vendor_id,
            'performance_data': serializer.data,
        })
