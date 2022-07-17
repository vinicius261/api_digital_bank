

import uuid
from django.db import models

from digital_bank.models.costumer import Costumer

"""Essa classe representa as transferências com todos os atributos
nscessários para registrar e realizar elas."""


class Transfer(models.Model):
    id_transfer = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requesting_costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='requesting', verbose_name='Cliente solicitante')
    favored_costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='favored',verbose_name='Cliente favorecido')
    date = models.DateTimeField(verbose_name='Data')
    value = models.FloatField()
    
    def __str__(self) -> str:
        return str(f"No valor de {self.value} em {self.date}")