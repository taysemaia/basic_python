# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia


def meu_in(valor, sequencia):
	 for i in range(len(sequencia)):
		 if valor == sequencia[i]:
			 return True
	 return False
# SE TIVER RETORNA TRUE, SE NÃO, RETORNA FALSE 

l1 = [1, 3, 4, 5]
l2 = [3, 2, 4, 5 ,6 ,7]
def tem_afinidade(l1, l2):
  aux = False
  contador = 0
  for i in range(len(l1)):
    contem = meu_in(l1[i], l2)
    if contem == True:
      contador += 1
  
  if contador >= 3:
    aux = not False
  else:
    aux = aux  
  
  return aux

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True





