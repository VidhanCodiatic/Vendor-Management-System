
from django.contrib import admin
from Vendors.models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = [
            'id', 'name', 'contact_details', 'address', 'vendor_code', 
            'on_time_delivery_rate', 'quality_rating_avg',
            'average_response_time', 'fulfillment_rate',
        ]
