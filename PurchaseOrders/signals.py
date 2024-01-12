
import random
import string

from django.db.models.signals import pre_save
from django.dispatch import receiver

from PurchaseOrders.models import PurchaseOrder


@receiver(pre_save, sender=PurchaseOrder)
def generate_po_number(sender, instance, *args, **kwargs):
    if not instance.po_number:
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10))
        instance.po_number = res

pre_save.connect(generate_po_number, sender=PurchaseOrder)




from django.dispatch import Signal, receiver
from performance_metrics.models import HistoricalPerformance

performance_history_model = HistoricalPerformance
purchase_order_status_completed = Signal()
purchase_order_acknowledged = Signal()


@receiver(signal=purchase_order_status_completed)
def calc_perfomance_matrix(sender, instance, **kwargs):
vendor = instance.vendor
on_time_delivery_rate = vendor.calc_on_time_delivery_rate()
quality_rating_avg = vendor.calc_avg_quality_ratings()
fulfillment_rate = vendor.calc_fulfillment_rate()

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from PurchaseOrders.models import PurchaseOrder
# from Vendors.models import Vendor
# from django.db import models

# @receiver(post_save, sender=PurchaseOrder)
# def update_on_time_delivery_rate(sender, instance, **kwargs):
#     if instance.status == 'completed':
#         vendor = instance.vendor
#         completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
#         on_time_deliveries = completed_orders.filter(delivery_date__lte=models.F('delivery_date'))
#         on_time_delivery_rate = (on_time_deliveries.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0.0
#         vendor.on_time_delivery_rate = on_time_delivery_rate
#         vendor.save()

# post_save.connect(update_on_time_delivery_rate, sender=PurchaseOrder)