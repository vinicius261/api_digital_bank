from digital_bank.models.costumer import Costumer
from digital_bank.support_code.clean_id import clean_id


"""Esse script contém código de tratamento e manipulação de dados para atualizar
os saldos na ralização das tranferências."""


def balance_udate(self, request):

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)

    balance = Costumer.objects.filter(
        id=clean_id(str(serializer.data['requesting_costumer']))).values_list('balance')

    new_balance = balance.get()[0] - serializer.data['value']

    new_balance = round(new_balance, 2)

    balance.update(balance=new_balance)

    favored_balance = Costumer.objects.filter(
        id=clean_id(str(serializer.data['favored_costumer']))).values_list('balance')

    new_favored_balance = favored_balance.get()[0] + serializer.data['value']

    new_favored_balance = round(new_favored_balance, 2)

    favored_balance.update(balance=new_favored_balance)

    return serializer.data, headers
