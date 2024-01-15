
import factory
from Vendors.tests.factories import VendorFactory
from PurchaseOrders.models import PurchaseOrder
from faker import Factory

faker = Factory.create()


class PurchaseOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchaseOrder

    vendor = factory.SubFactory(VendorFactory)
    po_number = factory.Sequence(lambda n: f'PO{n}')
    order_date = factory.Faker('date_time_this_year', tzinfo=None)
    delivery_date = factory.Faker('date_time_this_year', tzinfo=None)
    items = {'item1': 'details1', 'item2': 'details2'}
    quantity = factory.Faker('random_int', min=1, max=100)
    status = factory.Faker('random_element', elements=['pending', 'completed', 'canceled'])
    quality_rating = factory.Faker('pyfloat', positive=True)
    issue_date = factory.Faker('date_time_this_year', tzinfo=None)
    acknowledgment_date = factory.Faker('date_time_this_year', tzinfo=None)
