
from rest_framework import viewsets, status
from rest_framework.response import Response

from digital_bank.models.costumer import Costumer
from digital_bank.serializers.customer_serializer import CostumerSerializer


class CostumerViewSet(viewsets.ModelViewSet):
    """ Essa classe contém os parâmetros de customizção das visualizações do banco de dados
    dos clientes e das buscas por dados dos clientes."""
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer

    def destroy(self, request, pk=None):
        content = 'Não é possível deletar os dados.' 
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = f"O saldo atual do cliente {serializer.data['name']} é de R${serializer.data['balance']}"
        return Response(response, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        content = 'Não é possível alterar os dados.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        content = 'Não é possível alterar os dados.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
