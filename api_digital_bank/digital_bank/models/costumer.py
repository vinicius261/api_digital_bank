

import uuid
from django.db import models

"""Essa classe representa os clientes e suas contas com todos os atributos
nscessários para indentificar os cliente e realizar as transferências."""


class Costumer(models.Model):
    FISICAL = "CPF"
    LEGAL = "CNPJ"

    COSTUMER_CHOICES = [
        (FISICAL, 'CPF'),
        (LEGAL, 'CNPJ')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome", max_length=100)
    address = models.CharField("Endereço", max_length=200)
    phone = models.CharField("Telefone", max_length=14)
    email = models.EmailField("E-mail")
    balance = models.FloatField("Saldo", default=30.0, null=True)
    document = models.CharField(
        "Documento", max_length=4, choices=COSTUMER_CHOICES)
    cpf = models.CharField("CPF", max_length=11, null=True)
    cnpj = models.CharField("CNPJ", max_length=14, null=True)

    def __str__(self) -> str:
        return self.name
