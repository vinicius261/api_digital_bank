from django.test import TestCase
from rest_framework.test import APIClient

class TransferTestCase(TestCase):

    def test_input(self):

        transfer = {
        "requesting_costumer": "http://127.0.0.1:8000/cliente/52ce2afe-32f3-4efa-8b6e-566d7d6bd3fd/",
        "favored_costumer": "http://127.0.0.1:8000/cliente/bfa41dc1-8307-4002-9c37-1806c1f2795e/",
        "date": "2022-07-12T00:00:00-03:00",
        "value": 1
        }

        client = APIClient()        
        response = client.post('/transferencia/', transfer , format='json')

        self.assertEqual(response.status_code, 201)