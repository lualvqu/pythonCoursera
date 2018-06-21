def vogal(letra):
    vogais = ['a','e','i','o','u']
    retorno = False
    if vogais.count(letra.lower()):
        retorno = True 
    return retorno or False