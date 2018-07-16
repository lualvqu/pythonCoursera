largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
for x in range(altura):
    for y in range(largura):
        print('#', end='')
    print('\n', end='')