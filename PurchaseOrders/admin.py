
from django.contrib import admin
from PurchaseOrders.models import PurchaseOrder

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'po_number', 'vendor', 'order_date', 'delivery_date', 
        'items', 'quantity', 'status', 'quality_rating',
        'issue_date', 'acknowledgment_date',
    ]
