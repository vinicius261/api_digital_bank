from rest_framework import serializers

""" Esse script contem as os códigos de manipulaçao das validações dos dados 
recibidos dos sobre clientes"""


def validate_document(self, data):
    if (data.get("document") == "CPF") and (data.get("cpf") == None):
        raise serializers.ValidationError(
            {'CPF': 'Para pessoa física o CPF é obrigatório. Por favor, preecha o campo.'})
    elif (data.get("document") == "CNPJ") and (data.get("cnpj") == None):
        raise serializers.ValidationError(
            {'CNPJ': 'Para pessoa jurídica o CNPJ é obrigatório. Por favor, preecha o campo.'})

    if (data.get("document") == "CPF"):
        if len(data.get("cpf")) != 11:
            raise serializers.ValidationError(
                {'CPF': 'Por favor, insira apenas números.'})

    if (data.get("document") == "CNPJ"):
        if len(data.get("cnpj")) != 14:
            raise serializers.ValidationError(
                {'CNPJ': 'Por favor, insira apenas números'})

    return data


def phone_(self, phone):
    if len(phone) < 9:
        raise serializers.ValidationError('Por favor, insira o DDD')
    if len(phone) > 12:
        raise serializers.ValidationError(
            'Por favor, insira apenas os números com DDD')

    return phone


def name_(self, name):
    if len(name.split()) < 2:
        raise serializers.ValidationError('Por favor, Coloque nome completo.')
    if len(name) < 5:
        raise serializers.ValidationError('Por favor, Coloque nome completo.')

    return name


def balance_(self, balance):
    if balance != 30.0:
        raise serializers.ValidationError(
            'Saldo não é um campo manipulável. Deixe vazio')

    return balance


def address_(self, address):
    if len(address.split(',')) < 4:
        raise serializers.ValidationError(
            'Por favor, coloque: Rua, número, bairro e cidade. Todos separados por vírgula.')

    return address
