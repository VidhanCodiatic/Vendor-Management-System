
from rest_framework import status, viewsets
from rest_framework.response import Response
from Vendors.models import Vendor

from PurchaseOrders.models import PurchaseOrder
from PurchaseOrders.permissions import PurchaseOrderPermission
from PurchaseOrders.serializers import PurchaseOrderSerializer


class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [PurchaseOrderPermission]

    def perform_create(self, serializer):
        user = self.request.user
        vendor = Vendor.objects.get(user=user)
        serializer.save(vendor=vendor)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return response

        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found for the current user.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
