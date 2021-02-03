# coding: utf-8
# prog-1, 2018.2, UFCG
# Tayse Maia
# Calcula preço de venda

custo_entrada = float(raw_input())
percentual_indireta = int(raw_input())
percentual_desejado = int(raw_input())
percentual_imposto = float(raw_input())
percentual_comissoes = int(raw_input())
percentual_descontos = int(raw_input())
percentual_encargos = float(raw_input())

preco_venda = (custo_entrada + percentual_indireta * 100 + percentual_desejado * 100) * 100 / (100 - percentual_imposto - percentual_comissoes - percentual_descontos - percentual_encargos) 
inteiro = preco_venda // 1
resto = preco_venda % 1 
print preco_venda
print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (preco_venda, inteiro, resto)
