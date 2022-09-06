


from digital_bank.support_code.clean_id import clean_id_

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

    
def post_tranfers(self):

    customer_ = self.client.post('/cliente/', customer, format='json')
    customer_2 = self.client.post('/cliente/', customer2, format='json')
    transfer = {
        "requesting_costumer": customer_.data["url"],
        "favored_costumer": customer_2.data["url"],
        "value": 10.1
    }

    transfer2 = {
        "requesting_costumer": customer_2.data["url"],
        "favored_costumer": customer_.data["url"],
        "value": 15.3
    }

    transfer3 = {
        "requesting_costumer": customer_2.data["url"],
        "favored_costumer": customer_.data["url"],
        "value": 6.32
    }

    transfer_ = self.client.post(
        '/transferencia/', transfer, format='json', follow=True)
    transfer_2 = self.client.post(
        '/transferencia/', transfer2, format='json', follow=True)
    transfer_3 = self.client.post(
        '/transferencia/', transfer3, format='json', follow=True)



def post_tranfers_id(self):

        customer_ = self.client.post('/cliente/', customer, format='json')
        customer_2 = self.client.post('/cliente/', customer2, format='json')
        transfer = {
            "requesting_costumer": customer_.data["url"],
            "favored_costumer": customer_2.data["url"],
            "value": 10.1
        }

        transfer2 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "value": 15.3
        }

        transfer3 = {
            "requesting_costumer": customer_2.data["url"],
            "favored_costumer": customer_.data["url"],
            "value": 6.32
        }

        transfer_ = self.client.post(
            '/transferencia/', transfer, format='json', follow=True)
        transfer_2 = self.client.post(
            '/transferencia/', transfer2, format='json', follow=True)
        transfer_3 = self.client.post(
            '/transferencia/', transfer3, format='json', follow=True)

        id = clean_id_(str(customer_.data["url"]))

        return id        