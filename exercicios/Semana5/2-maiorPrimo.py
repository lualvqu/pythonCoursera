from math import sqrt
def maior_primo(num):    
    for y in range (num, 0, -1):
        achou = False
        #Divide o numero n por todos os numeros de 2 até sua raiz quadrada+1
        for x in range(2, int(sqrt(y))+1):
            if (y % x == 0):
                achou = True
                break
        #Verifica se foi divisivel por algum numero
        if not achou:
            return y
