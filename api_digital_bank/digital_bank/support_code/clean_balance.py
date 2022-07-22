"""Esse script contém código que auxilia na manipulação de dados para atualizar
os saldos na ralização das tranferências. Ele transforma a resposta recebida em "balance" 
tornando a testagem da busca do saldo do cliente possível"""


def clean_balance(link: str):

    message = link.split('$')

    balance = float(message[1])

    return balance