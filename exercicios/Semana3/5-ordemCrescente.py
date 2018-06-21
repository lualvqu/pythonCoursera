lista = []
for x in range(3):
    lista.append(int(input()))
if lista[0] < lista[1] and lista[1] < lista[2]:
    print('crescente')
else:
    print('não está em ordem crescente')
