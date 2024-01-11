from django.db.models import Avg, Count
from datetime import timedelta
from PurchaseOrders.models import PurchaseOrder
from django.db import models

def calculate_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_orders.filter(delivery_date__lte=models.F('delivery_date'))
    on_time_delivery_rate = (on_time_deliveries.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0.0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()

def calculate_quality_rating_avg(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(quality_rating=None)
    quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
    vendor.quality_rating_avg = quality_rating_avg
    vendor.save()

# def update_average_response_time(vendor):
#     acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, status='acknowledged')
#     response_times = [po.acknowledgment_date - po.issue_date for po in acknowledged_orders]
#     avg_response_time = sum(response_times, timedelta()) / len(response_times) if len(response_times) > 0 else timedelta(0)
#     vendor.average_response_time = avg_response_time.total_seconds() / 3600  # Convert to hours
#     vendor.save()

# def update_fulfillment_rate(vendor):
#     total_orders = PurchaseOrder.objects.filter(vendor=vendor)
#     completed_orders = total_orders.filter(status='completed')
#     fulfillment_rate = (completed_orders.count() / total_orders.count()) * 100 if total_orders.count() > 0 else 0.0
#     vendor.fulfillment_rate = fulfillment_rate
#     vendor.save()


# def calculate_on_time_delivery_rate(db: Session, vendor_id: int):
#     total_completed_pos = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id,
#         PurchaseOrder.status == 'completed'
#     ).count()

#     on_time_deliveries = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id,
#         PurchaseOrder.status == 'completed',
#         PurchaseOrder.delivery_date <= PurchaseOrder.acknowledgment_date
#     ).count()

#     return on_time_deliveries / total_completed_pos if total_completed_pos > 0 else 0.0

# def calculate_quality_rating_avg(db: Session, vendor_id: int):
#     completed_pos = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id,
#         PurchaseOrder.status == 'completed',
#         PurchaseOrder.quality_rating.isnot(None)
#     ).all()

#     total_ratings = sum(po.quality_rating for po in completed_pos) if completed_pos else 0
#     return total_ratings / len(completed_pos) if len(completed_pos) > 0 else 0.0

# def calculate_average_response_time(db: Session, vendor_id: int):
#     pos_with_acknowledgment = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id,
#         PurchaseOrder.acknowledgment_date.isnot(None)
#     ).all()

#     total_response_time = sum(
#         (po.acknowledgment_date - po.issue_date).total_seconds()
#         for po in pos_with_acknowledgment
#     ) if pos_with_acknowledgment else 0.0

#     return total_response_time / len(pos_with_acknowledgment) if len(pos_with_acknowledgment) > 0 else 0.0

# def calculate_fulfillment_rate(db: Session, vendor_id: int):
#     total_pos = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id
#     ).count()

#     fulfilled_pos = db.query(PurchaseOrder).filter(
#         PurchaseOrder.vendor_id == vendor_id,
#         PurchaseOrder.status == 'completed',
#         PurchaseOrder.quality_rating.is_(None)  # Assuming only successful ones are considered
#     ).count()

#     return fulfilled_pos / total_pos if total_pos > 0 else 0.0