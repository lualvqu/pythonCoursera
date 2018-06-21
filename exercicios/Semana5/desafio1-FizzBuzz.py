def fizzbuzz(x):
    retorno = ''
    if x % 3 == 0:
        retorno = retorno + 'Fizz'
    if x % 5 == 0:
        retorno = retorno + 'Buzz'
    if retorno == '':
        retorno = x
    return retorno