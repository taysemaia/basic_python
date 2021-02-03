# coding: utf-8
#Tayse de Oliveira Maia
#Matrícula: 117110028
# Prog-1, 2018.2
# Aprovvação Unidades

unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))

proxima_unidade = unidade + 1
msg = 'O aluno vai para a unidade %d com média %.1f.'

print msg % (proxima_unidade, media)
