"""Esse script contém código qu auxilia na manipulação de dados para atualizar
os saldos na ralização das tranferências. Ele transforma a URL recebida em "id" 
tornando a busca do saldo do cliente possível"""


def clean_id(link: str):

    url = link.split('/')

    uuid = url[4]

    return uuid
