
# from rest_framework.test import APITestCase

# null = None

# customer = {
#     "cpf": "40122912589",
#     "cnpj": null,
#     "name": "Vinicius Santos",
#     "address": "Rua Lira, 569, Jd. Sta, Ubatuba",
#     "phone": "1123569877",
#     "email": "vinicius2@hotmail.com",
#     "document": "CPF"
# }

# customer1 = {
#     "cpf": null,
#     "cnpj": "12345678912345",
#     "name": "Padaria LTDA",
#     "address": "Rua Lira, 569, Jd. Sta, São PAulo",
#     "phone": "1123569899",
#     "email": "pao@hotmail.com",
#     "document": "CNPJ"
# }

# transfer = {
#             "requesting_costumer": customer_.data["url"],
#             "favored_costumer": customer_2.data["url"],
#             "date": "2022-07-12T00:00:00",
#             "value": 10.1
#         }

# transfer2 = {
#             "requesting_costumer": customer_2.data["url"],
#             "favored_costumer": customer_.data["url"],
#             "date": "2019-07-12T00:00:00",
#             "value": 15.3
#         }        

# transfer = {
#             "requesting_costumer": customer_2.data["url"],
#             "favored_costumer": customer_.data["url"],
#             "date": "2019-07-12T00:00:00",
#             "value": 6.32
#         }        

# class FiltersTestCase(APITestCase):

#     def test_send_transfers(self):

#         response = self.client.post('/consulta/?customer_.data["url"]', customer, format='json')

    