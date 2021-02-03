# coding: utf-8
# programação 1, período 2018-2, UFCG
# Tayse Maia
# Caixas de Morango

morangos = float(raw_input())

caixas = morangos // 400
resto = morangos % 400
porcentagem = resto / morangos * 100

print "Serão necessárias %d caixa(s) para embalar os morangos." % caixas 
print "%.1f%% dos morangos serão perdidos." % porcentagem
