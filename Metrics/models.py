
from django.db import models
from Vendors.models import Vendor


class HistoricalPerformance(models.Model):
    '''
    This model optionally stores historical data on vendor performance, enabling trend analysis
    '''
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
