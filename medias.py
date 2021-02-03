# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia
# Aula de médias

soma = 0.0
numeros = [] 

while True:
  numero = float(raw_input())
  soma += numero
  numeros.append(numero)

  if soma >= 100:
    break

media = soma / len(numeros)
print "Quantidade de números lidos: %d" % len(numeros)
print "Soma dos números lidos: %.2f" % soma
print "Média = %.2f" % media

print ""

print "Abaixo da média"
for i in range(len(numeros)): 
  if numeros[i] < media:
    print "%.2f (%do)" % (numeros[i], i+1)

print ""
print "Acima da média"

for j in range(len(numeros)):
  if numeros[j] > media:
    print "%.2f (%do)" % (numeros[j], j+1)
