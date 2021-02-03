# coding: utf-8
# prog-1, 2018-2
# Tayse de Oliveira Maia
# Área do Cilindro 

import math

print "Cálculo da Superfície de um Cilindro"
print "---"
diametro = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))

raio = diametro / 2
areabase = math.pi * (raio ** 2)
arealateral = altura * ( 2 * math.pi * raio)
suptotal = (2 * areabase) + arealateral
print "---"
print "Área calculada: %.2f" % suptotal
