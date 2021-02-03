# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia 
# Conjunto com mais elementos

numero = []
soma = 0.0

while True:
  numeros = raw_input()
  if numeros == 'fim':
    break 
  soma += 1
  if int(numeros) < 0:
    numero.append(soma)
    soma = 0.0
     
 
for i in range(len(numero)):
  numero[i] = numero[i] - 1

maior = max(numero)
indice = numero.index(maior)

print "Conjunto %d - %d elemento(s)" % (indice + 1, numero[indice]) 

