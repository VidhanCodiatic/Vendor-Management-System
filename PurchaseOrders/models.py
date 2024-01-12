
from django.core.exceptions import ValidationError
from django.db import models
from Vendors.models import Vendor


class PurchaseOrder(models.Model):
    '''
    This model captures the details of each purchase order and is used to calculate various
    performance metrics.
    '''
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add = True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add = True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
    def clean(self):
        super().clean()

        if (
            self.quantity < 0 or
            self.quality_rating < 0
        ):
            raise ValidationError("Values cannot be negative.")
        
        if self.delivery_date <= self.order_date:
            raise ValidationError("Delivery date must be greater than order date.")
        
        if self.acknowledgment_date < self.issue_date:
            raise ValidationError("Acknowledgment date cannot be before the issue date.")
