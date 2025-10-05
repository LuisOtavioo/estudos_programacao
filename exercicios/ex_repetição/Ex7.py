#Faça um programa que calcule o mostre a média aritmética de N notas, com N dado pelo usuário.
print("CALCULADORA DE MÉDIAS")

while True: #Pedir quantidade de notas
    try:
        quantidade_notas = int(input("Digite a quantidade de notas: "))
        if quantidade_notas > 0:
            break
        else:
            print("Digite um número maior que zero!")
    except ValueError:
        print("Por favor, digite apenas números!")

soma = 0  

for i in range(quantidade_notas):   #Coletar cada nota
    while True:
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            if 0 <= nota <= 10:
                soma += nota
                break
            else:
                print("Nota inválida! Digite entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número!")


#resultado
media = soma / quantidade_notas 

print(f"\nRESULTADO:")
print(f"Total de notas: {quantidade_notas}")
print(f"Soma das notas: {soma}")
print(f"Sua média é: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado! \n")
else:
    print("Situação: Reprovado. \n")
    exit()