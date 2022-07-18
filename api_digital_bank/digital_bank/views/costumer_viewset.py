
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from digital_bank.models.costumer import Costumer
from digital_bank.serializers.customer_serializer import CostumerSerializer

""" Essa classe contém os parâmetros de customizção das visualizações do banco de dados
dos clientes e das buscas por dados dos clientes."""


class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer
    permission_classes = [permissions.IsAuthenticated] #isautenticated?

    def destroy(self, request, pk=None):
        return Response({'menssagem': 'Não é possível deletar os dados.'})        

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = f"O saldo atual do cliente {serializer.data['name']} é de R${serializer.data['balance']}."
        return Response({response})  
    
    def partial_update(self, request, pk=None): 
        return Response({'Não é possível alterar os dados.'}) 

    def update(self, request, pk=None): 
        return Response({'Não é possível alterar os dados.'}) 