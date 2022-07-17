API REST DIGITAL BANK

● Visão geral

Essa API REST é uma simplificação de um banco digital que realiza as 
seguintes ações:

    ● A criação de uma nova conta
    ● Consulta de todas as contas criadas
    ● Consulta de saldo de um conta
    ● Transferência de saldo entre contas
    ● Consulta das transferências de uma conta (Recebidos e enviados)
        ○ Com a possibilidade de consultar em um dado período estipulado
    ● Consulta do saldo de uma conta

Ela foi criada na linguagem python com uso  do framework Django Rest Framework.

● Como usar

    ● Acessando a API

        Utilize o métodoo GET nessa URL:
            http://127.0.0.1:8000/

        A resposta será a seguinte:

        HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "cliente": "http://127.0.0.1:8000/cliente/",
            "tranferencia": "http://127.0.0.1:8000/tranferencia/"
        }

        Na tela inicial existe o acesso para o cadastro dos cliente e transferências.

    
    ● Criando uma nova conta e consultando todas a contas

        Utilize o métodoo POST nessa URL:
            http://127.0.0.1:8000/cliente/

        O corpo da requisição deve ser no formato:

        {
        "name": "",        
        "address": "",      
        "phone": "",        
        "email": "",       
        "balance": null,        
        "document": "Pessoa física",    """ OU   "document": "Pessoa jurídica" """
        "cpf": "",          
        "cnpj": ""
        }      

        A resposta será:    

            HTTP 201 Created
            Allow: GET, POST, HEAD, OPTIONS
            Content-Type: application/json
            Location: http://127.0.0.1:8000/cliente/dcc3458d-a803-4a89-9f99-f3b5f346b33c/
            Vary: Accept

            {
                "url": "http://127.0.0.1:8000/cliente/dcc3458d-a803-4a89-9f99-f3b5f346b33c/",
                "name": "Lucas Silva",
                "address": "Rua Lira, 369, Santa Efigenia, Rio",
                "phone": "11996568988",
                "email": "lu@email.com.br",
                "balance": 30.0,
                "document": "CPF",
                "cpf": "45698956412",
                "cnpj": null
            }

        Para consultar todas as contas utilize o métodoo GET nessa URL:        
            http://127.0.0.1:8000/cliente/

        A resposta será:
            HTTP 200 OK
            Allow: GET, POST, HEAD, OPTIONS
            Content-Type: application/json
            Vary: Accept

            {
                "count": 5,
                "next": null,
                "previous": null,
                "results": []
            }



    ● Consultando de saldo de um conta

        Para consultar o saldo de uma conta utilize o métodoo GET nessa URL com 
        o "id" do cliente:        
            http://127.0.0.1:8000/cliente/

            ex: http://127.0.0.1:8000/cliente/52ce2afe-32f3-4efa-8b6e-566d7d6bd3fd/

        A resposta será:

            HTTP 200 OK
            Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
            Content-Type: application/json
            Vary: Accept

            [
                "O saldo atual do cliente Padaria LTDA é de R$30.0."
            ]

    ● Transferindo de saldo entre contas

        Para realizer a trasnferência de saldo entre contas utilize o métodoo POST
        nessa URL:        
            http://127.0.0.1:8000/tranferencia/

        O corpo da requisição deve ser no formato:

            {
                "requesting_costumer": "",
                "favored_costumer": "",
                "date": "",
                "value": ""
            }

        Os campos "requesting_costumer" e "favored_costumer" devem ser preenchidos
        com as URLs de, respectivamente, o cliente solicitante e o cliente favorecido.

        A URL deve se no formato "http://127.0.0.1:8000/cliente/52ce2afe-32f3-4efa-8b6e-566d7d6bd3fd/"
        onde o que vem depois do "/cliente/" é o "id" do cliente.

        A resposta será:

            HTTP 201 Created
            Allow: GET, POST, HEAD, OPTIONS
            Content-Type: application/json
            Location: http://127.0.0.1:8000/tranferencia/6d233da4-ca99-42e5-b9b6-267c228fe305/
            Vary: Accept

            {
                "url": "http://127.0.0.1:8000/tranferencia/6d233da4-ca99-42e5-b9b6-267c228fe305/",
                "requesting_costumer": "http://127.0.0.1:8000/cliente/52ce2afe-32f3-4efa-8b6e-566d7d6bd3fd/",
                "favored_costumer": "http://127.0.0.1:8000/cliente/bfa41dc1-8307-4002-9c37-1806c1f2795e/",
                "date": "2022-07-17T16:23:00-03:00",
                "value": 15.0
            }

    ● Consultando as transferências de uma conta 

        Para realizar as consultas das tranferência de uma conta deve-se usar o
        método GET na URL:
            http://127.0.0.1:8000/consulta/

        Isso listará todas as tranferências do banco.Para filtrar por cliente deve 
        ser especificado após o "/consulta/?" como deseja realizar a consulta.

        Para filrar todas as transferências realizadas coloque o  "requesting_costumer="
        seguido "id" do cliente a ser consutado.

        Já para filrar todas as transferências recebidas coloque o  "favored_costumer="
        seguido "id" do cliente a ser consutado.

        Assim como no exemplo:
            /consulta/?favored_costumer=bfa41dc1-8307-4002-9c37-1806c1f2795e        

        Filtar por períodos exige que álem do "id" coloque outras especificações
        que estão detalhadas a seguir:

        "date__gte=" para consultar maior ou igual que uma certa data
        "date__lte=" para consultar menor ou igual que uma certa data
        "date__gt=" para consultar maior que uma certa data
        "date__lt=" para consultar menor que uma certa data

        O formato inserido deve ser 2022-07-18T00:00:00

        Para separa as especificações use "&".

        A consulta a seguir tras todas as transferências recebidas do cliente
        entre 18/07/22 e30/07/22:
            /consulta/?date__gte=2022-07-18T00:00:00&date__lte=2022-07-30T23:59:59&favored_costumer=bfa41dc1-8307-4002-9c37-1806c1f2795e


    ● Consultando o saldo de uma conta 

    Para consultar o saldo de uma conte deve-se utilizar o método GET na URL a
    seguir com o "id" do cliente após o"/cliente":
        http://127.0.0.1:8000/cliente/52ce2afe-32f3-4efa-8b6e-566d7d6bd3fd/

