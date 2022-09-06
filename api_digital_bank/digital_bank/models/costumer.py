

import uuid
from django.db import models

from digital_bank.support_code.costumer_name import costumer_name


class Costumer(models.Model):
    """Essa classe representa os clientes e suas contas com todos os atributos
    nescessários para indentificar os cliente e realizar as transferências."""

    COSTUMER_CHOICES = [
        ('CPF', 'CPF'),
        ('CNPJ', 'CNPJ')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome", max_length=100)
    address = models.CharField("Endereço", max_length=200)
    phone = models.CharField("Telefone", max_length=14)
    email = models.EmailField("E-mail")
    balance = models.FloatField("Saldo", default=30.0, null=True)
    document = models.CharField(
        "Documento", max_length=8, choices=COSTUMER_CHOICES)
    cpf = models.CharField("CPF", max_length=11, null=True)
    cnpj = models.CharField("CNPJ", max_length=14, null=True)

    def __str__(self) -> str:
        return costumer_name(self)
