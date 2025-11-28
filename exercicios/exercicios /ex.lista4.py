'''Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Armazene os números
pares na lista PAR e os números ímpares na lista IMPARES. Imprima as 3 listas'''
import random

numeros = []
pares = []
impares = []

for i in range(20):
    numero_lido = random.randint(1, 20)
    numeros.append(numero_lido)

    if numero_lido % 2 == 0:
        pares.append(numero_lido)
    else:
        impares.append(numero_lido)

print(f'lista de numeros: {numeros}')
print(f'numeros pares: {pares}')
print(f'numeros impares: {impares}')
