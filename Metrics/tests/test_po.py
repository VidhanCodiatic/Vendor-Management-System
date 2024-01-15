
import faker
from faker import Factory

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from PurchaseOrders.models import PurchaseOrder
from Vendors.tests.factories import UserFactory, VendorFactory

faker = Factory.create()

class PurchaseOrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()

        self.vendor = VendorFactory(user=self.user)
        self.client.force_authenticate(user=self.user)
     

    def test_create_purchase_order(self):
        url = '/api/purchase_orders/'

        data = {
            'delivery_date': faker.date_time().isoformat(),
            'items': {'item1': faker.text(max_nb_chars=20), 
                      'item2': faker.text(max_nb_chars=20)
            },
            'quantity': faker.random.randint(1,10),
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_create_purchase_order_unauthenticated(self):
        self.client.logout()

        url = '/api/purchase_orders/'

        data = {
            'delivery_date': faker.date_time().isoformat(),
            'items': {'item1': faker.text(max_nb_chars=20), 
                      'item2': faker.text(max_nb_chars=20)
            },
            'quantity': faker.random.randint(1,10),
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def tearDown(self):
        PurchaseOrder.objects.all().delete()





from django.test import TestCase
from rest_framework.test import APIClient
from Vendors.tests.factories import VendorFactory
from Metrics.tests.factories import HistoricalPerformanceFactory

class VendorPerformanceViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_vendor_performance_view(self):
        # Create a vendor and historical performance data for the vendor
        vendor = VendorFactory()
        historical_performance = HistoricalPerformanceFactory(vendor=vendor)

        # Make a GET request to your API endpoint
        response = self.client.get(f'/api/vendor_performance/{vendor.id}/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the expected structure of the response JSON
        expected_data = {
            'vendor_id': vendor.id,
            'performance_data': [
                {
                    'id': historical_performance.id,
                    'vendor': vendor.id,
                    'date': historical_performance.date.isoformat(),
                    'on_time_delivery_rate': str(historical_performance.on_time_delivery_rate),
                    'quality_rating_avg': str(historical_performance.quality_rating_avg),
                    'average_response_time': str(historical_performance.average_response_time),
                    'fulfillment_rate': str(historical_performance.fulfillment_rate),
                }
            ]
        }
        self.assertEqual(response.json(), expected_data)



