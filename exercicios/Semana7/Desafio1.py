def n_primos(param):
    cont = 0
    for x in range (2, param+1):
        dividiu = False
        for y in range(2, x):
            if x % y == 0:
                dividiu = True
        if not dividiu:
            cont += 1
            print(x, end='\t')
    return cont