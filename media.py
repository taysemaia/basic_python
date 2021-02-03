# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia
# Acima da média (CRIMINALIDADE)

def media_sequencia(sequencia):
  valores = sequencia.split()
  soma = 0.0
  for valor in valores:
    soma += int(valor)
  return soma / len(valores)

media_estabelecida = float(raw_input())

sequencias = []

while True:
  seq = raw_input()
  if seq == "fim" or media_sequencia(seq) < media_estabelecida / 2:
    break
  sequencias.append(seq)

medias = []
for seq in sequencias:
  medias.append(media_sequencia(seq))

acima_limite = [] 

for i in range(len(sequencias)):
  if medias[i] > media_estabelecida:
    acima_limite.append(sequencias[i])

for j in acima_limite:
  print j
