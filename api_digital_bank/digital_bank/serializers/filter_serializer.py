from rest_framework import serializers
from digital_bank.models.transfer import Transfer

"""Essa classe faz a serialização dos dados das consultas sobre transferências."""

class FilterTransferSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Transfer
        fields = ['url','id_transfer', 'requesting_costumer', 'favored_costumer', 'date', 'value']