

from rest_framework import serializers
from digital_bank.models.costumer import Costumer
from digital_bank.validators.costumer_validator import *


class CostumerSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe faz as validações dos dados de entrada dos clientes e a serialização."""

    balance = serializers.FloatField(read_only=True)
    cpf = serializers.CharField(allow_null=True)
    cnpj = serializers.CharField(allow_null=True)

    class Meta():
        model = Costumer
        fields = "__all__"

    def validate(self, data):
        return validate_document(self, data)

    def validate_phone(self, phone):
        return phone_(self, phone)

    def validate_name(self, name):
        return name_(self, name)

    def validate_address(self, address):
        return address_(self, address)

    def validate_balance(self, balance):
        return balance_(self, balance)
