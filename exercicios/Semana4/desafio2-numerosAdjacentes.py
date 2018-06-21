numero = input('Digite um número inteiro: ')
valida = False
for x in range(len(numero)-1):
    if numero[x] == numero[x+1]:
        valida = True
        break

if valida:
    print('sim')
else:
    print('não')