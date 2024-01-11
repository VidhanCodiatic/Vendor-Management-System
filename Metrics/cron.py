
from django.core.management.base import BaseCommand
from django.utils import timezone
from Vendors.models import Vendor
from Metrics.models import HistoricalPerformance
from PurchaseOrders.calculate import (
    calculate_on_time_delivery_rate, calculate_quality_rating_avg,
)

def my_cron_job():
    print('this is crone job fun')

# class Command(BaseCommand):
#     help = 'Generates historical performance records'

#     def handle(self, *args, **options):
#         print('hello crontab')
#         vendors = Vendor.objects.all()

#         for vendor in vendors:
#             # Perform calculations for historical performance metrics based on your logic
#             on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
#             quality_rating_avg = calculate_quality_rating_avg(vendor)
#             # ...other metrics

#             # Create a new historical performance record
#             HistoricalPerformance.objects.create(
#                 vendor=vendor,
#                 date=timezone.now(),
#                 on_time_delivery_rate=on_time_delivery_rate,
#                 quality_rating_avg=quality_rating_avg,
#                 # ...other metrics
#             )

#         self.stdout.write(self.style.SUCCESS('Successfully generated historical performance records'))
# # Run the management command every day at midnight
# 0 0 * * * /path/to/your/venv/bin/python /path/to/your/project/manage.py generate_historical_performance
# chmod +x /path/to/your/project/manage.py
        

# python manage.py crontab add
# python manage.py crontab show
# python manage.py crontab remove
