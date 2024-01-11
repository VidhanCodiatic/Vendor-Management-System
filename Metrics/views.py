
from Metrics.models import HistoricalPerformance
from Metrics.serializers import HistoricalPerformanceSerializer
from rest_framework import viewsets, generics

# class HistoricalPerformanceModelViewSet(viewsets.ModelViewSet):
#     queryset = HistoricalPerformance.objects.all()
#     serializer_class = HistoricalPerformanceSerializer

class VendorHistoricalPerformanceView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import HistoricalPerformance
# from .serializers import HistoricalPerformanceSerializer
# from Vendors.models import Vendor

# @api_view(['GET'])
# def vendor_performance_view(request, vendor_id):
#     vendor = Vendor.objects.get(pk=vendor_id)
#     performances = HistoricalPerformance.objects.filter(vendor=vendor)
#     serializer = HistoricalPerformanceSerializer(performances, many=True)
#     return Response(serializer.data)