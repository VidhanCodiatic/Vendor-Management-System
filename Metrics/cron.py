
from django.utils import timezone
from PurchaseOrders.calculate import (calculate_average_response_time,
                                      calculate_fulfillment_rate,
                                      calculate_on_time_delivery_rate,
                                      calculate_quality_rating_avg)
from Vendors.models import Vendor

from Metrics.models import HistoricalPerformance

# python manage.py crontab add
# python manage.py crontab run id
# python manage.py crontab show
# python manage.py crontab remove

# 12 am, pm every day */12   *    *    * 
# */1 * * * * for every minute


def my_cron_job():
    vendors = Vendor.objects.all()

    for vendor in vendors:
        # vendor_id = vendor.id
        on_time_delivery_rate = vendor.on_time_delivery_rate
        quality_rating_avg = vendor.quality_rating_avg
        avg_response_time = vendor.average_response_time
        fulfillment_rate = vendor.fulfillment_rate

        historical_performance_list = [
            HistoricalPerformance(
                vendor=vendor,
                date=timezone.now(),
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                average_response_time=avg_response_time,
                fulfillment_rate=fulfillment_rate,
            ),
        ]


        HistoricalPerformance.objects.bulk_create(historical_performance_list)




        # on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
        # quality_rating_avg = calculate_quality_rating_avg(vendor)
        # avg_response_time = calculate_average_response_time(vendor_id)
        # fullfillment_time = calculate_fulfillment_rate(vendor_id)

        # HistoricalPerformance.objects.create(
        #     vendor=vendor,
        #     date=timezone.now(),
        #     on_time_delivery_rate=on_time_delivery_rate,
        #     quality_rating_avg=quality_rating_avg,
        #     average_response_time=avg_response_time,
        #     fulfillment_rate=fullfillment_time
        # )


#bulk create code optimization
