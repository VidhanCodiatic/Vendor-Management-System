
import factory
from datetime import datetime, timedelta
from Metrics.models import HistoricalPerformance
from Vendors.tests.factories import VendorFactory
from faker import Factory

faker = Factory.create()

class HistoricalPerformanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HistoricalPerformance

    vendor = factory.SubFactory(VendorFactory)
    date = factory.Faker('date_time_this_month')
    on_time_delivery_rate = factory.Faker('pyfloat', positive=True)
    quality_rating_avg = factory.Faker('pyfloat', positive=True)
    average_response_time = factory.Faker('pyfloat', positive=True)
    fulfillment_rate = factory.Faker('pyfloat', positive=True)

