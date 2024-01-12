from rest_framework import serializers

from PurchaseOrders.models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = [
            'id', 'po_number', 'vendor', 'order_date', 'delivery_date', 
            'items', 'quantity', 'status', 'quality_rating',
            'issue_date', 'acknowledgment_date',
        ]
        read_only_fields = [
            'id', 'po_number', 'vendor', 'order_date',
            'status', 'quality_rating', 'issue_date',
            'acknowledgment_date',
        ]