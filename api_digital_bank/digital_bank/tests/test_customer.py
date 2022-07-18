from django.test import TestCase
from rest_framework.test import APIClient

class CostumerTestCase(TestCase):

    def test_input(self):

        customer = {
        "name": "Silva e Silva",
        "address": "Rua da, 51, Jardim, SP",
        "phone": "5512569877",
        "email": "silva@sem.com",
        "balance": "30",
        "document": "CPF",
        "cpf": "40122569847",
        "cnpj": None
        }

        client = APIClient()        
        response = client.post('/cliente/', customer , format='json')

        self.assertEqual(response.status_code, 201)
        # client = RequestsClient()
        # response = client.get('http://testserver/users/')
        # assert response.status_code == 201