
from rest_framework.test import APITestCase

from digital_bank.support_code.clean_balance import clean_balance


customer2 = {
        "cpf": "40122912522",
        "cnpj": "12345678912345",
        "name": "Vinicius Mira",
        "address": "Rua Lira, 569, Jd. Sta, São PAulo",
        "phone": "1123569899",
        "email": "vinicius@hotmail.com",
        "document": "CPF"
    }

customer = {
        "cpf": "40122912589",
        "cnpj": "12345678912345",
        "name": "Vinicius Mira",
        "address": "Rua Lira, 569, Jd. Sta, São PAulo",
        "phone": "1123569899",
        "email": "vinicius@hotmail.com",
        "document": "CPF"
    }


class TransferTestCase(APITestCase):


    def test_input(self):

        response_c1 = self.client.post('/cliente/', customer, format='json')
        response_c2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": response_c1.data["url"],
            "favored_costumer": response_c2.data["url"],
            "date": "2022-07-12T00:00:00-03:00",
            "value": 10.1
        }

        response = self.client.post('/transferencia/', transfer, format='json', follow= True)

        self.assertEqual(response.status_code, 201)

    def test_balance(self):

        response_c1 = self.client.post('/cliente/', customer, format='json')
        response_c2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": response_c1.data["url"],
            "favored_costumer": response_c2.data["url"],
            "date": "2022-07-12T00:00:00-03:00",
            "value": 10.1
        }

        response = self.client.post('/transferencia/', transfer, format='json', follow= True)

        response_c2_get = self.client.get(response_c2.data["url"] , format='json', follow= True)

        saldo = clean_balance(response_c2_get.data)

        self.assertEqual(saldo, 40.1)