n = int(input('Digite o valor de n: '))
fatorial = 1
for x in range(n, 1, -1):
    fatorial = fatorial * x
print(fatorial)