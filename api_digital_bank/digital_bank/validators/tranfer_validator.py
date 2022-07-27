from rest_framework import serializers

""" Esse script contem as os códigos de manipulaçao das validações dos dados 
recibidos dos sobre tranferências."""


def balance_(self, data):

    requesting_costumer = (data.get('requesting_costumer'))
    balance = requesting_costumer.balance
    value = (data.get('value'))

    if balance < value:
        raise serializers.ValidationError(
            {'Saldo': 'O saldo é insuficiente para realizar a transferência.'})

    return data


def value_(self, value):

    if value < 0:
        raise serializers.ValidationError(
            'O valor da transferência precisa ser um valor positivo.')

    if type(value) != float:
            raise serializers.ValidationError(
                'Insira apenas números e separe apenas por ponto (ex: 31.57).')        

    return value
