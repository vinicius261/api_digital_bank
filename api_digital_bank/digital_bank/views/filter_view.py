from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from digital_bank.models.transfer import Transfer
from digital_bank.serializers.filter_serializer import FilterTransferSerializer



class TransferListView(generics.ListAPIView):
    """ Essa classe contém os parâmetros de filtragem e busca de dados no banco de
    de dados de transferências."""

    queryset = Transfer.objects.all()
    serializer_class = FilterTransferSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       OrderingFilter, SearchFilter)
    filterset_fields = {'date': ['gte', 'lte', 'exact', 'gt', 'lt'],
                        'requesting_costumer': ['exact'], 'favored_costumer': ['exact']}

    orderind_fields = ('date')
    ordering = ('date')
    search_fields = ('requesting_costumer', 'favored_costumer',)
