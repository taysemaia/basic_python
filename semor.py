# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia
# Aprovados e Reprovados

num_alunos_aprovados = 0
num_alunos_reprovados = 0
soma_notas_reprovados = 0
soma_notas_aprovados = 0

num_alunos = int(raw_input())

for aluno in range(num_alunos):
    nota = float(raw_input())
    if nota >= 7:
        num_alunos_aprovados += 1
        soma_notas_aprovados += nota
    else:
        soma_notas_reprovados += nota
        num_alunos_reprovados +=1
if num_alunos_reprovados > 0:
  media1 = soma_notas_reprovados / num_alunos_reprovados
  print"Reprovados:", num_alunos_reprovados
  print"Média: %.1f" % media1
  print 
else:
  print"Reprovados:", num_alunos_reprovados
  print
if num_alunos_aprovados > 0:
  media2 = soma_notas_aprovados / num_alunos_aprovados
  print"Aprovados:", num_alunos_aprovados
  print"Média: %.1f" % media2
else:
  print"Aprovados:", num_alunos_aprovados

