# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia
# Autorização de voos

tempo_voos = int(raw_input())
quantidade_avioes = int(raw_input())
tempodevoos = []
autorizados = []
soma = 0 

for i in range(quantidade_avioes):
  tempo_cada = int(raw_input())
  tempodevoos.append(tempo_cada)
  tempodevoos.sort()

for j in tempodevoos:
  soma += j
  if soma <= tempo_voos:
    autorizados.append(1)



print len(autorizados),"voo(s) autorizados." 
