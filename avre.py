# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia
# Arvore Natal

altura = int(raw_input())
larguramax = 2 * altura - 1 

for alturas in range(altura + 1):
	print ' ' * (larguramax - ( 2 * alturas - 1) / 2),
	print 'o' * (2 * alturas - 1)
print (larguramax + 1) * " " + "o"

