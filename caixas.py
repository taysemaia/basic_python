# coding: utf-8
# programação 1, período 2018-2, UFCG
# Tayse Maia
# Caixas Ceramica 

capacidade = float(raw_input("Capacidade de revestimento? "))
print ""
print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

chao = comprimento * largura
parede = altura * comprimento
total = chao + 4 * parede
caixas = total / capacidade
print ""
print "== Resultados =="
print "Área total a revestir: %.1f m2" % total
print "Número de caixas: %d" % caixas 

