#Faça um Programa que peça o raio de um círculo como float, calcule e mostre sua área. 
#Para usar a constante pi no programa, no insira no início do código: from math import pi

from math import pi

print("Vamos calcular a área do circulo?")
raio = float(input("Qual é o raio do círculo? \n "))

# Calcula a área
area = pi * (raio**2)

#resultado
print(f"A área do círculo é {area}!")

