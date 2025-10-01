#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

#pare são numeros múltiplos exatos de 2
#então se ao dividirmos por 2 tiver resto, será impar

for i in range(1, 51):
    if i % 2 != 0:  # Verifica se o resto da divisão por 2 é diferente de zero
        print(i)