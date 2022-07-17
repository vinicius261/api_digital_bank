
from rest_framework import serializers
from digital_bank.models.transfer import Transfer
from digital_bank.validators.tranfer_validator import balance_

"""Essa classe faz as validações dos dados de entrada das transferências e a serialização."""

class TransferSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Transfer
        fields = ['url', 'requesting_costumer', 'favored_costumer', 'date', 'value']

    def validate(self, data):
        content = balance_(self, data)
        return content      

    # def validate_date(self, date):
    #     content = date_(self, date)
    #     return content    