# coding: utf-8
# Programação 1, UFCG, 2018.2
# Tayse de Oliveira Maia
# Melhor ataque

times = int(raw_input())
total_gols = 0.0
time = []
gols = [] 
maior = 0
vencedor = " "

for i in range(times):
 nome = raw_input()
 numero_gols = int(raw_input())
 total_gols += numero_gols 
 time.append(nome)
 gols.append(numero_gols)

 if numero_gols == maior:
   vencedor += "\n" + nome
 elif numero_gols > maior: 
   vencedor = nome 
   maior = numero_gols

media = total_gols / times

print "Time(s) com melhor ataque (%d gol(s)):" % maior
print vencedor
print
print "Média de gols marcados: %.1f" % media 

