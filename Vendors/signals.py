import random

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from Metrics.models import HistoricalPerformance
from PurchaseOrders.calculate import (calculate_average_response_time,
                                      calculate_fulfillment_rate,
                                      calculate_on_time_delivery_rate,
                                      calculate_quality_rating_avg)
from Vendors.models import Vendor


@receiver(pre_save, sender=Vendor)
def generate_vendor_code(sender, instance, *args, **kwargs):
    if not instance.vendor_code:
        base_code = slugify(instance.name+str(random.randint(0,99999)))
        vendor_code = base_code
        suffix = 1  # Initialize suffix
        while Vendor.objects.filter(vendor_code=vendor_code).exists():
            vendor_code = f"{base_code}-{suffix}"
            suffix += 1
        instance.vendor_code = vendor_code

pre_save.connect(generate_vendor_code, sender=Vendor)

@receiver(post_save, sender=Vendor)
def calculate_perfomance(sender, instance, **kwargs):
    vendor = instance.id
    on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
    quality_rating_avg = calculate_quality_rating_avg(vendor)
    average_response_time = calculate_average_response_time(vendor)
    fulfillment_rate = calculate_fulfillment_rate(vendor)


    instance.on_time_delivery_rate = on_time_delivery_rate
    instance.quality_rating_avg = quality_rating_avg
    instance.average_response_time = average_response_time
    instance.fulfillment_rate = fulfillment_rate

post_save.connect(calculate_perfomance, sender=Vendor)










# from django.dispatch import Signal, receiver
# from performance_metrics.models import HistoricalPerformance

# performance_history_model = HistoricalPerformance
# purchase_order_status_completed = Signal()
# purchase_order_acknowledged = Signal()

    # on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
    # quality_rating_avg = calculate_quality_rating_avg(vendor)
    # avg_response_time = calculate_average_response_time(vendor_id)
    # fullfillment_rate = calculate_fulfillment_rate(vendor_id)
    # vendor.refresh_from_db()

    # HistoricalPerformance.objects.create(
    # vendor=vendor,
    # on_time_delivery_rate=on_time_delivery_rate,
    # quality_rating_avg=quality_rating_avg,
    # fulfillment_rate=fulfillment_rate,
    # average_response_time=vendor.average_response_time,
    # )
    # return vendor