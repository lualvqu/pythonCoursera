#  ======  Receiving Values  ======
nome            = input('Digite o nome do cliente: ')
diaVencimento   = input('Digite o dia de vencimento: ')
mesVencimento   = input('Digite o mês de vencimento: ')
valorFatura     = input('Digite o valor da fatura: ')

#  ======  Printing Informations  ======
print('Olá, {0}\nA sua fatura com vencimento em {1} de {2} no valor de R$ {3} está fechada.'.format(nome, diaVencimento, mesVencimento, valorFatura))