def costumer_name(self):
    if self.document == 'Physical':
            documment = f'{self.name} - {self.cpf}'
    else:
        documment = f'{self.name} - {self.cnpj}'
    return documment