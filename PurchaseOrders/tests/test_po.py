
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


