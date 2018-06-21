#  ======  Receiving the input  ======
segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

#  ======  Calculating  ======

# ===   Days    ===
dias        = segundos // 86400
segundos    = segundos % 86400
# ===   Hours   ===
horas       = segundos // 3600
segundos    = segundos % 3600
# ===  Minutes  ===
minutos     = segundos // 60
segundos    = segundos % 60

#  ======  Printing Informations  ======
print('{0} dias, {1} horas, {2} minutos e {3} segundos.'.format(dias, horas, minutos, segundos))

