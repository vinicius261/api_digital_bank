
from rest_framework import viewsets, permissions, status
from django_filters import *
from django_filters import rest_framework as filters
from rest_framework.response import Response
from digital_bank.models.transfer import Transfer
from digital_bank.serializers.transfer_serializer import TransferSerializer
from digital_bank.views.costumer_viewset import CostumerViewSet
from digital_bank.support_code.clean_id import clean_id
from digital_bank.support_code.balace_updates import balance_udate

""" Essa classe contém os parâmetros de customizção das visualizações do banco de dados
dos clientes e das buscas por dados das tranferências."""


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # filter_backends = (filters.DjangoFilterBackend)
    # filterset_fiels = ('data', 'requesting_costumer', 'favored_costumer')
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        content, headers = balance_udate(self, request)          
        return Response (content, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        return Response({'Não é possível deletar os dados.'})
    
    def partial_update(self, request, pk=None): 
        return Response({'Não é possível alterar os dados.'}) 

    def update(self, request, pk=None): 
        return Response({'Não é possível alterar os dados.'}) 


   
  