# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia 
# Analytics assembleia

def conta_votos(votacoes,id_votacao):
  sim = 0
  nao = 0
  for i in range(len(votacoes)):
    lista = votacoes[i].split(',')
    if lista[2] == str(id_votacao):
      if lista[1] == 'sim':
        sim += 1
      else:
        nao += 1    
  lista_numeros = []
  lista_numeros.append(sim)
  lista_numeros.append(nao)
  return lista_numeros

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')

assert conta_votos(votacao, 99) == [1,0]


