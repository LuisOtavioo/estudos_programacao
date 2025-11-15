#Faça um programa que peça 10 números inteiros, calcule e mostre a 
#quantidade de números pares e aquantidade de números impares.

pares = 0
impares = 0
QUANTIDADE_TOTAL = 10

print("---Início da Coleta de Números---")

for i in range(QUANTIDADE_TOTAL):
    numero = int(input(f"Digite o {i + 1}º número de {QUANTIDADE_TOTAL}: "))

    if numero % 2 == 0:
        pares += 1
    elif numero % 2 != 0:
        impares += 1

print("\n" + ("=" * 15) + " Resultados " + ("=" * 15))
print(f"A quantidade de números pares é: {pares}")
print(f"A quantidade de números ímpares é: {impares}")
print("=" * 42)