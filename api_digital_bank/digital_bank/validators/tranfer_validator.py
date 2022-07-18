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
