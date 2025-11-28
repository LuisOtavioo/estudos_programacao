'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. Refaça a
função para que também retorno ‘Z’ se o argumento for nulo.'''

import sys

def soma(a, b, c):
    return a + b + c


valor1 = float(input('Digite um número real: '))
valor2 = float(input('Digite outro número real: '))
valor3 = float(input('Digite mais um número real: '))

resultado = soma(valor1, valor2, valor3)

if resultado > 0:
    print('\nP') #positivo
elif resultado <= 0:
    print('\nN') #negativo
else:
    print('\nZ') #nulo

sys.exit