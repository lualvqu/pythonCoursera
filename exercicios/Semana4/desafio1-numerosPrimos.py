from math import sqrt

n = int(input('Digite um número inteiro: '))
achou = False

#Divide o numero n por todos os numeros de 2 até sua raiz quadrada+1
for x in range(2, int(sqrt(n))+1):
    if (n % x == 0):
        achou = True
        break

#Verifica se foi divisivel por algum numero
if achou:
    print('não primo')
else:
    print('primo')