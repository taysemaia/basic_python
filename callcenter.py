# coding: utf-8
# prog1, 2018.2, UFCG
# Tayse Maia
# Callcenter

segunda = int(raw_input())
terca = int(raw_input())
quarta = int(raw_input())
quinta = int(raw_input())
sexta = int(raw_input())
sabado = int(raw_input())
domingo = int(raw_input())

total = segunda + terca + quarta + quinta + sexta + sabado + domingo
media = total / 7.0

print "Total:", total 
print "Média: %.2f" % media
