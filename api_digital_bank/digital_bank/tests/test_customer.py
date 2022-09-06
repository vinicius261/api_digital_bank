

from rest_framework.test import APITestCase
from digital_bank.support_code.customer_test import customer, customer1


class CostumerTestCase(APITestCase):
    """ Essa classe realiza os testes sobre as ações possíveis em relação aos
    clientes."""

    def test_input(self):

        response = self.client.post('/cliente/', customer, format='json')

        self.assertEqual(response.status_code, 201)

    def test_get(self):

        post_test = self.client.post('/cliente/', customer, format='json')
        post_test2 = self.client.post('/cliente/', customer1, format='json')

        response = self.client.get('/cliente/')

        self.assertTrue(response.data["count"] == 2)

    def test_get_balance(self):

        post_test = self.client.post('/cliente/', customer, format='json')

        response = self.client.get(
            post_test.data["url"], format='json', follow=True)

        self.assertEqual(
            response.data, f"O saldo atual do cliente Vinicius Santos é de R$30.0")

    def test_detroy(self):

        post_test = self.client.post('/cliente/', customer, format='json')

        response = self.client.delete(
            post_test.data["url"], format='json', follow=True)

        self.assertEqual(response.status_code, 405)

    def test_partial_update(self):
        request = {
            "phone": "1123569874",
        }

        post_test = self.client.post('/cliente/', customer, format='json')

        response = self.client.patch(
            '/cliente/', request, format='json', follow=True)

        self.assertEqual(response.status_code, 405)

    def test_update(self):
        post_test = self.client.post('/cliente/', customer, format='json')

        response = self.client.put(
            '/cliente/', customer1, format='json', follow=True)

        self.assertEqual(response.status_code, 405)
