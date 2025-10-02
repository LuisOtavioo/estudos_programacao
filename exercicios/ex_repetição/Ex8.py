#Faça um programa que calcule o mostre a média aritmética de N notas, com N dado pelo usuário. 
#O usuário deve fornecer pelo menos 3 notas, e o programa encerrado se ele informar um N<3
#Excluindo da média: a maior e menor nota.

import sys
print("CALCULADORA DE MÉDIAS")

quantidade_notas = int(input('quantidade de notas'))


if quantidade_notas < 3:
	sys.exit('número de notas insuficiente')


soma = 0  

while True:
	nota = float(input(f"Digite a nota {i+1}: "))
	if 0 <= nota <= 10:
		break 

maior_nota = nota
menor_nota = nota

for i in range(1,quantidade_notas):  #Coletar cada nota
	while True:
		nota = int(input(f"Digite a nota {i+1}: "))
		if 0 <= nota <= 10:
			break 
	soma += nota
	maior_nota = nota if nota > maior_nota else maior_nota
	menor_nota = nota if nota < menor_nota else menor_nota
    

#resultado
media = (soma - menor_nota - maior_nota) / (quantidade_notas - 2)

print(f"\nRESULTADO:")
print(f"Total de notas: {quantidade_notas}")
print(f"Soma das notas: {soma}")
print(f"Sua média é: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado! \n")
else:
    print("Situação: Reprovado. \n")
    exit()