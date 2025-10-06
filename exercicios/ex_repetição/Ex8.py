#Faça um programa que calcule o mostre a média aritmética de N notas, com N dado pelo usuário.
#O usuário deve fornecer pelo menos 3 notas, e o programa encerrado se ele informar um N<3
#Excluindo da média: a maior e menor nota. 

import sys

print("---CALCULADORA DE MÉDIAS 2.0---")

quantidade_notas = int(input('Quantidade de notas (mínimo 3): '))

if quantidade_notas < 3:
    sys.exit('Número de notas insuficiente (mínimo 3). Encerrando o programa.')

notas = [] # Lista para armazenar as notas

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a nota {i + 1} de {quantidade_notas} (entre 0 e 10): "))
        
        if 0 <= nota <= 10:
            notas.append(nota)
            break  
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
            
# Cálculo e Exclusão 
maior_nota = max(notas)
menor_nota = min(notas)

soma_total = sum(notas)

soma_ajustada = soma_total - maior_nota - menor_nota

media = soma_ajustada / (quantidade_notas - 2)

# Resultado
print(f"\n{'='*25}\nRESULTADO FINAL\n{'='*25}")
print(f"Maior nota (Excluída): {maior_nota:.2f}")
print(f"Menor nota (Excluída): {menor_nota:.2f}")
print(f"Média Calculada: {media:.2f}")

if media >= 6:
    print("\nSituação: Aprovado! Parabéns!")
else:
    print("\nSituação: Reprovado.")