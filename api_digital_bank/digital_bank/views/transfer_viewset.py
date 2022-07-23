
from rest_framework import viewsets,  status
from django_filters import *
from rest_framework.response import Response

from digital_bank.models.transfer import Transfer
from digital_bank.serializers.transfer_serializer import TransferSerializer
from digital_bank.support_code.balace_updates import balance_udate

""" Essa classe contém os parâmetros de customizção das visualizações do banco de dados
dos clientes e das buscas por dados das tranferências."""


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def create(self, request, *args, **kwargs):
        content, headers = balance_udate(self, request)
        return Response(content, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        content = 'Não é possível deletar os dados.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def partial_update(self, request, pk=None):
        content = 'Não é possível alterar os dados.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def update(self, request, pk=None):
        content = 'Não é possível alterar os dados.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
