# coding: utf-8
# prog-1, 2018-2
# Tayse de Oliveira Maia
# Açudes

captotal = int(raw_input("capacidade? ")) # metros cubicos
percentual_atual = float(raw_input("percentual hoje? "))
consumo_dia = int(raw_input("gasto diário? "))

porcent = percentual_atual / 100
vol_atual = porcent * captotal
diasrest = int(vol_atual // consumo_dia)

print "volume: %.2f" % vol_atual
print "dias restantes:", diasrest
