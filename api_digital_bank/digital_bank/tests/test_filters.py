

from rest_framework.test import APITestCase

from digital_bank.support_code.clean_id import clean_id_

""" Essa classe realiza os testes sobre as ações possíveis em relação aos
as consultas de transferências."""

null = None

customer = {
    "cpf": "40122912589",
    "cnpj": null,
    "name": "Vinicius Santos",
    "address": "Rua Lira, 569, Jd. Sta, Ubatuba",
    "phone": "1123569877",
    "email": "vinicius2@hotmail.com",
    "document": "CPF"
}

customer2 = {
    "cpf": null,
    "cnpj": "12345678912345",
    "name": "Padaria LTDA",
    "address": "Rua Lira, 569, Jd. Sta, São PAulo",
    "phone": "1123569899",
    "email": "pao@hotmail.com",
    "document": "CNPJ"
}


class FiltersTestCase(APITestCase):

    def test_transfers_between(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')
        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-12-12T00:00:00",
            "value": 10.1
        }

        transfer2 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 15.3
        }

        transfer3 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-01-12T00:00:00",
            "value": 6.32
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)
        transfer_2 = self.client.post(
            '/transferencia/', transfer2, format='json', follow=True)
        transfer_3 = self.client.post(
            '/transferencia/', transfer3, format='json', follow=True)

        response = self.client.get(
            '/consulta/?date__gte=2022-06-18T00:00:00&date__lte=2022-12-30T23:59:59', format='json')

        self.assertTrue(response.data["count"] == 2)

    def test_transfers_received(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')
        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-12-12T00:00:00",
            "value": 10.1
        }

        transfer2 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 15.3
        }

        transfer3 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-01-12T00:00:00",
            "value": 6.32
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)
        transfer_2 = self.client.post(
            '/transferencia/', transfer2, format='json', follow=True)
        transfer_3 = self.client.post(
            '/transferencia/', transfer3, format='json', follow=True)

        id = clean_id_(str(customer_.data["url"]))

        response = self.client.get(
            f'/consulta/?favored_costumer={id}', format='json')

        self.assertTrue(response.data["count"] == 2)

    def test_transfers_sent(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')
        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-12-12T00:00:00",
            "value": 10.1
        }

        transfer2 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 15.3
        }

        transfer3 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-01-12T00:00:00",
            "value": 6.32
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)
        transfer_2 = self.client.post(
            '/transferencia/', transfer2, format='json', follow=True)
        transfer_3 = self.client.post(
            '/transferencia/', transfer3, format='json', follow=True)

        id = clean_id_(str(customer_.data["url"]))

        response = self.client.get(
            f'/consulta/?requesting_costumer={id}', format='json')

        self.assertTrue(response.data["count"] == 1)

    def test_transfers_between_for_costumer(self):
        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')
        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "date": "2022-12-12T00:00:00",
            "value": 10.1
        }

        transfer2 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-07-12T00:00:00",
            "value": 15.3
        }

        transfer3 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "date": "2022-01-12T00:00:00",
            "value": 6.32
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)
        transfer_2 = self.client.post(
            '/transferencia/', transfer2, format='json', follow=True)
        transfer_3 = self.client.post(
            '/transferencia/', transfer3, format='json', follow=True)

        id = clean_id_(str(customer_.data["url"]))

        response = self.client.get(
            f'/consulta/?date__gte=2022-01-01T00:00:00&date__lte=2022-12-30T23:59:59&requesting_costumer={id}', format='json')

        self.assertTrue(response.data["count"] == 1)
