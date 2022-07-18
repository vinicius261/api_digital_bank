

from rest_framework import serializers
from digital_bank.models.costumer import Costumer
from digital_bank.validators.costumer_validator import *


"""Essa classe faz as validações dos dados de entrada dos clientes e a serialização."""


class CostumerSerializer(serializers.HyperlinkedModelSerializer):
    balance = serializers.FloatField(read_only=True)
    cpf = serializers.CharField(allow_null=True)
    cnpj = serializers.CharField( allow_null=True)

    class Meta():
        model = Costumer
        fields = "__all__"
        
    def validate(self, data):
        content = validate_document(self, data)
        return content
    def validate_phone(self, phone):
        content = phone_(self, phone)
        return content

    def validate_name(self, name):
        content = name_(self, name)
        return content

    def validate_address(self, address):
        content = address_(self, address)
        return content
            

    def validate_balance(self, balance):
        content = balance_(self, balance)
        return content
