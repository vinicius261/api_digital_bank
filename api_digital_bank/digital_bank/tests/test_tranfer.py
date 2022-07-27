

from rest_framework.test import APITestCase

from digital_bank.support_code.clean_balance import clean_balance

""" Essa classe realiza os testes sobre as ações possíveis em relação aos
clientes."""

null = None

customer = {
    "cpf": "40122912522",
    "cnpj": null,
    "name": "Vinicius Santos",
    "address": "Rua Lira, 1347, Jd. Sta, Ubatuba",
    "phone": "1123569899",
    "email": "vinicius2@hotmail.com",
    "document": "CPF"
}

customer2 = {
    "cpf": "40122912589",
    "cnpj": null,
    "name": "Vinicius Santos",
    "address": "Rua Lira, 569, Jd. Sta, São PAulo",
    "phone": "1123569899",
    "email": "vinicius@hotmail.com",
    "document": "CPF"
}


class TransferTestCase(APITestCase):

    def test_input(self):

        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 10.1
        }

        response = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)

        self.assertEqual(response.status_code, 201)

    def test_balance_updates(self):

        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 10.1
        }

        response = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)

        customer_2_get = self.client.get(
            customer_2.data["url"], format='json', follow=True)

        saldo = clean_balance(customer_2_get.data)

        self.assertEqual(saldo, 40.1)

    def test_detroy(self):

        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 10.1
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)

        response = self.client.delete(
            transfer_.data["url"], format='json', follow=True)

        self.assertEqual(response.status_code, 405)

    def test_partial_update(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 10.1
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)

        request = {
            "value": 550315,
        }

        response = self.client.patch(
            transfer_.data["url"], request, format='json', follow=True)

        self.assertEqual(response.status_code, 405)

    def test_update(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')

        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 10.1
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)

        transfer_update = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2019-07-12T00:00:00",
            "value": 5000
        }

        response = self.client.put(
            '/transferencia/', transfer_update, format='json', follow=True)

        self.assertEqual(response.status_code, 405)
