#Starting Variable
notaAux = 0
#Defining dic list for the print
dic = ['primeira', 'segunda', 'terceira', 'quarta']
#Receiving all values
for y in range(4):
    notaAux = notaAux + int ( input ( 'Digite a {} nota: '.format(dic[y]) ) )
#Printing the score average
print('A média aritmética é {}'.format(notaAux/4))