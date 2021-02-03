# coding: utf-8
# Programação 1, 2018.2
# Tayse de Oliveira Maia 
# Calculadora


while True:
  numeros = raw_input().split()
  
  if int(numeros[0]) == 5:
    break
  
  elif int(numeros[0]) == 1:
    soma = int(numeros[1]) + int(numeros[2])
    
    print soma
  
  elif int(numeros[0]) == 2:
    sub = int(numeros[1]) - int(numeros[2])
    
    print sub
  
  elif int(numeros[0]) == 3:
    multi = int(numeros[1]) * int(numeros[2])
   
    print multi
  
  elif int(numeros[0]) == 4:  
    
    if int(numeros[2]) == 0:
      print "Erro: Divisão por 0"
      break
    
    div = int(numeros[1]) / int(numeros[2])
    
    print div
