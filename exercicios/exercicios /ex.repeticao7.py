#Faça um programa que calcule o mostre a média aritmética de N notas, com N dado pelo usuário.
print("---CALCULADORA DE MÉDIAS---")

while True: 
    
    quantidade_notas = int(input("Digite a quantidade de notas (mínimo 1): "))
    
    if quantidade_notas > 0:
        break
    else:
        print("Quantidade inválida! Digite um número maior que zero.")

soma = 0  

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a nota {i+1} de {quantidade_notas} (entre 0 e 10): "))
        
        if 0 <= nota <= 10:
            soma += nota
            break # Nota válida, sai do loop e vai para a próxima
        else:
            print("Nota inválida! Digite um valor entre 0 e 10 e tente novamente.")


media = soma / quantidade_notas 

# Resultado 
print(f"\nRESULTADO:")
print(f"Total de notas: {quantidade_notas}")
print(f"Soma das notas: {soma:.2f}")
print(f"Sua média é: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado! \n")
else:
    print("Situação: Reprovado. \n")