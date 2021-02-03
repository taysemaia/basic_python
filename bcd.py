# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia, 117110028
# Binary Coded Decimal


BCD = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001']

sequencias = []

while True:
  sequencia = raw_input()
  if sequencia == 'fim':
    break
  sequencias.append(sequencia)
  
for i in range(len(sequencias)): 
  parte_1 = sequencias[i][0:4]
  parte_2 = sequencias[i][4:8]
  if len(sequencias[i]) != 8.0:
    print "Tente novamente."
  elif parte_1 in BCD and parte_2 in BCD:
    print str(int(parte_1, 2)) + str(int(parte_2, 2))
  else:
    print "BCD inválido."

