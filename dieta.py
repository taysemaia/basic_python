# coding: utf-8 
# prog-1 ufcg 
# Tayse Maia 
# Dias de dieta

peso = float(raw_input())
horas = float(raw_input())
calorias = float(raw_input())

dia1 = (calorias - (900 * horas) - 2000) * (-1)
calorias_perder = peso * 7700
dias = calorias_perder / dia1

print "Você precisará de %.2f dias de dieta" % dias 




