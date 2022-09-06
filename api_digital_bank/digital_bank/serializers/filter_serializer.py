from rest_framework import serializers
from digital_bank.models.transfer import Transfer


class FilterTransferSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe faz a serialização dos dados das consultas sobre transferências."""

    class Meta():
        model = Transfer
        fields = ['url', 'id_transfer', 'requesting_costumer',
                  'favored_costumer', 'date', 'value']
