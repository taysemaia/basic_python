# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia 
# Analytics votação

def conta_votos(votacoes, id):
  sim = 0
  nao = 0
  for i in range(len(votacoes)):
    lista = votacoes[i].split(',')
    if lista[2] == str(id):
      if lista[1] == 'sim':
        sim += 1
      else:
        nao += 1    
  lista_numeros = []
  lista_numeros.append(sim)
  lista_numeros.append(nao)
  return lista_numeros





