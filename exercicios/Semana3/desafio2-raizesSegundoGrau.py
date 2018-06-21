from math import sqrt
a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if (delta < 0):
    print ('esta equação não possui raízes reais')
elif (delta == 0):
    print('a raiz desta equação é {0}'.format((-(b)+sqrt(delta))/(2*a)))
else:
    raizes = []
    raizes.append((-(b)+sqrt(delta))/(2*a)) 
    raizes.append((-(b)-sqrt(delta))/(2*a)) 
    print('as raízes da equação são {0} e {1}'.format(min(raizes), max(raizes)))