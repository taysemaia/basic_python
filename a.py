# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia

def organiza_por_media(lista):
  somador = 0
  lista_menor = []
  lista_maior = []
  if lista == []:
    return []

  for listas in lista:
    somador += listas
  media = somador / len(lista)

  for listas in lista:
    if listas <= media:
      lista_menor.append(listas)
    else:
      lista_maior.append(listas)
  lista_nova = lista_menor + lista_maior
  
  for i in range(len(lista)):
      lista[i] = lista_nova[i]
  
  return lista

p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
assert p1 == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]

