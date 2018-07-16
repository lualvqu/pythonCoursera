largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
for x in range(altura):
    for y in range(largura):
        if x==0 or x==altura-1 or y==0 or y==largura-1:
            print('#', end='')
        else:
            print(' ', end='')
    print('\n', end='')