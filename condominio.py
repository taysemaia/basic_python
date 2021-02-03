# coding: utf-8
# prog1, 2018.2, UFCG
# Tayse Maia
# Construção de condomínio 

lado1 = float(raw_input())
lado2 = float(raw_input())
area_casa = float(raw_input())

area_terreno = lado1 * lado2 
quantidade = area_terreno // area_casa

print "%d casa(s) pode(m) ser construída(s) no terreno." % quantidade

