
from django.db.models import Count, F, Sum

from PurchaseOrders.models import PurchaseOrder

# def calculate_quality_rating_avg(vendor):
#     completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(quality_rating=None)
#     quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
#     vendor.quality_rating_avg = quality_rating_avg
#     vendor.save()


# optimization date  

def calculate_on_time_delivery_rate(vendor):
    ven_id = vendor
    # vendor = Vendor.objects.get(id=vendor)
    total_completed_pos = PurchaseOrder.objects.filter(
        vendor=ven_id, status='completed').count()

    on_time_deliveries = PurchaseOrder.objects.filter(
        vendor=ven_id, status='completed', delivery_date__lte=F('acknowledgment_date')).count()
    
    return on_time_deliveries / total_completed_pos if total_completed_pos > 0 else 0.0


def calculate_quality_rating_avg(vendor):
    ven_id = vendor

    quality_rating_data = PurchaseOrder.objects.filter(
        vendor=ven_id, status='completed',
        quality_rating__gt=0
    ).aggregate(
        total_ratings=Sum('quality_rating'),
        total_orders=Count('id')
    )

    total_ratings = quality_rating_data['total_ratings'] if quality_rating_data['total_ratings'] else 0
    total_orders = quality_rating_data['total_orders'] if quality_rating_data['total_orders'] else 1  # Prevent division by zero

    return total_ratings / total_orders

def calculate_average_response_time(vendor):
    ven_id = vendor
    pos_with_acknowledgment = PurchaseOrder.objects.filter(
        vendor=ven_id, status='completed',
        quality_rating__gt=0
    ).all()

    total_response_time = sum(
        (po.acknowledgment_date - po.issue_date).total_seconds()
        for po in pos_with_acknowledgment
    ) if pos_with_acknowledgment else 0.0

    print(total_response_time / len(pos_with_acknowledgment) if len(pos_with_acknowledgment) > 0 else 0.0)

    return total_response_time / len(pos_with_acknowledgment) if len(pos_with_acknowledgment) > 0 else 0.0

def calculate_fulfillment_rate(vendor):
    ven_id = vendor
    total_pos = PurchaseOrder.objects.filter(
        vendor = ven_id
    ).count()

    fulfilled_pos = PurchaseOrder.objects.filter(
        vendor = ven_id,
        status = 'completed',
        quality_rating__gt=0  # Assuming only successful ones are considered
    ).count()

    return fulfilled_pos / total_pos if total_pos > 0 else 0.0







# Returns:
# - str: The username of the user.
# """
# return self.email 

# def calc_on_time_delivery_rate(self):
# po_list = self.purchaseorder_set.filter(status="completed")
# filter_on_time_deliverables = po_list.filter(
# acknowledgment_date__lte=models.F("delivery_date")
# )
# try:
# return round(filter_on_time_deliverables.count() / po_list.count(), 2)
# except ZeroDivisionError:
# return 0

# def calc_avg_quality_ratings(self):
# po_list = self.purchaseorder_set.filter(status="completed")
# result = po_list.aggregate(
# avg_quality_rating=models.Avg("quality_rating", default=0.0)
# )

# return round(result.get("avg_quality_rating"))

# def calc_fulfillment_rate(self):
# po_list_status_completed = self.purchaseorder_set.filter(status="completed")

# po_list = self.purchaseorder_set.filter(status="pending")

# try:
# return round(po_list_status_completed.count() / po_list.count(), 2)
# except ZeroDivisionError:
# return 0

# def calc_avg_response_time(self):
# filter_po_data = self.purchaseorder_set.filter(
# issue_date__isnull=False, acknowledgment_date__isnull=False
# )

# if filter_po_data.exists():
# result = filter_po_data.aggregate(
# avg_response_time=models.Avg(
# models.F("acknowledgment_date") - models.F("issue_date")
# )
# )
# try:
# return round(result.get("avg_response_time").total_seconds(), 2)
# except ZeroDivisionError:
# return 0