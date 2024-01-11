
from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    '''
    This model stores essential information about each vendor and their performance metrics.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='vender_name')
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
        # return f"{self.name} - {self.id}"

#     def save(self, *args, **kwargs):
#         if not self.vendor_code:
#             base_code = slugify(self.name)
#             vendor_code = base_code
#             suffix = 1
#             while Vendor.objects.filter(vendor_code=vendor_code).exists():
#                 vendor_code = f"{base_code}-{suffix}"
#                 suffix += 1
#             self.vendor_code = vendor_code
#         super().save(*args, **kwargs)

