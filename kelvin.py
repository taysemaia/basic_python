# coding: utf-8
# Tayse de OLiveira Maia
# Matrícula: 117110028
# Programação 1, turma 3, 2018.2
# Conversor Fahrenheit Celsius Kelvin

Fah = raw_input()
Fah= float(Fah)
Cel = (Fah - 32) * 5/9 
Kel = Cel + 273.15  

Kel = "%.3f" % Kel
Cel = "%.3f" % Cel
Fah =  "%.3f" % Fah

print "Fahrenheit:" ,Fah, "F"
print "Celsius:" ,Cel, "C"
print "Kelvin:" ,Kel, "K" 
