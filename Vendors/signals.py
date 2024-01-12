import random

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

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
