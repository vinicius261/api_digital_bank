

from rest_framework import serializers
from digital_bank.models.transfer import Transfer
from digital_bank.validators.tranfer_validator import balance_, value_


class TransferSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe faz as validações dos dados de entrada das transferências e a serialização."""

    class Meta():
        model = Transfer
        fields = ['url', 'requesting_costumer',
                  'favored_costumer', 'date', 'value']

    def validate(self, data):
        content = balance_(self, data)
        return content

    def validate_value(self, value):
        content = value_(self, value)
        return content
