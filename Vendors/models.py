
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Vendor(models.Model):
    '''
    This model stores essential information about each vendor and their performance metrics.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='vender_name')
    name = models.CharField(max_length=100)
    contact_details = models.TextField(unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()

        if len(self.contact_details) not in [10, 12]:
            raise ValidationError({'contact_details': 'Contact details must be either 10 or 12 characters long.'})

        if not self.contact_details.isdigit():
            raise ValidationError({'contact_details': 'Contact details must contain only numeric characters.'})

        if (
            self.on_time_delivery_rate < 0 or
            self.quality_rating_avg < 0 or
            self.average_response_time < 0 or
            self.fulfillment_rate < 0
        ):
            raise ValidationError("Values cannot be negative.")
        

