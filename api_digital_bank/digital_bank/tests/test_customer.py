
from rest_framework.test import APITestCase

null = None

customer = {
    "cpf": "40122912589",
    "cnpj": null,
    "name": "Vinicius Mira",
    "address": "Rua Lira, 569, Jd. Sta, São PAulo",
    "phone": "1123569899",
    "email": "vinicius@hotmail.com",
    "document": "CPF"
}

customer1 = {
    "cpf": "40122912874",
    "cnpj": null,
    "name": "Aurelio Mira",
    "address": "Rua Lira, 569, Jd. Sta, São PAulo",
    "phone": "1123569899",
    "email": "vinicius@hotmail.com",
    "document": "CPF"
}

class CostumerTestCase(APITestCase):

    def test_input(self):

        response = self.client.post('/cliente/', customer, format='json')

        self.assertEqual(response.status_code, 201)

    def test_get(self):

        post1 = self.client.post('/cliente/', customer, format='json')
        post2 = self.client.post('/cliente/', customer1, format='json')

        response = self.client.get('/cliente/')

        self.assertTrue(response.data["count"] == 2 )    

    def test_detroy(self):

        post1 = self.client.post('/cliente/', customer, format='json')

        response = self.client.delete('/cliente/', customer, format='json', follow= True)

        self.assertEqual(response.status_code, 405)    

    def test_partial_update(self):
        request = {
        "phone": "1123569874",
        }

        post1 = self.client.post('/cliente/', customer, format='json')

        response = self.client.patch('/cliente/', request, format='json', follow= True)

        self.assertEqual(response.status_code, 405)    

    def test_update(self):
        post1 = self.client.post('/cliente/', customer, format='json')

        response = self.client.put('/cliente/', customer1, format='json', follow= True)

        self.assertEqual(response.status_code, 405)    


    #  def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     response = f"O saldo atual do cliente {serializer.data['name']} é de R${serializer.data['balance']}."
    #     return Response({response})   

    # def test_detroy_msg(self):


    #         post1 = self.client.post('/cliente/', customer, format='json')

    #         response = self.client.delete('/cliente/', customer, format='json', follow= True)

    #         self.assertTrue(response.content['menssagem'], {'menssagem': 'Não é possível deletar os dados.'})    