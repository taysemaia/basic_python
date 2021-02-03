# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia, 117110028
# Caixa Preta


peso = []
combustivel = []
altitude = []

while True:
  lista = raw_input().split()
  peso.append(lista[0])
  combustivel.append(lista[1])
  altitude.append(lista[2])
  
  if int(lista[0]) < 0 or int(lista[1]) < 0 or int(lista[2]) < 0:
    break
    
validos_p = []
negativos_p = 0.0

for i in range(len(peso)):
 
  if int(peso[i]) < 0:
    print "dado inconsistente. peso negativo."
    negativos_p +=1
    
  elif int(peso[i]) >= 0:
    validos_p.append(peso[i])

validos_c = []
negativos_c = 0

for j in range(len(combustivel)):
  
  if int(combustivel[j]) < 0:
    print "dado inconsistente. combustível negativo."
    negativos_c += 1
    
  elif int(combustivel[j]) >= 0:
    validos_c.append(combustivel[j])   

validos_a = []
negativos_a = 0

for k in range(len(altitude)):
  
  if int(altitude[k]) < 0:
    print "dado inconsistente. altitude negativa."
    negativos_a += 1
    
  elif int(altitude[k]) >= 0:
    validos_a.append(altitude[k])

if negativos_p > 0:
  validos_c.pop()
  validos_a.pop()

elif negativos_c > 0:
  validos_a.pop()



print "peso: %d" % len(validos_p)
print "combustível: %d" % len(validos_c)
print "altitude: %d" % len(validos_a)
