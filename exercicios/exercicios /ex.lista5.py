'''Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação em uma lista.
Imprima'''

nome = []
idade = []
altura = []

contagem = 0


while True:
    if contagem < 5:
        print(f"\n--- Participante {contagem + 1 } de 5 ---")
        n = input('\nDígite seu nome: ')
        nome.append(n)
   
        i = int(input('Dígite sua idade: '))
        idade.append(i)

        a = float(input('Digite sua altura: '))
        altura.append(a)
        contagem += 1
    else:
        break

'''print("\n" + "-"*50)
print("\nparticipantes: ",nome)
print("Idades: ",idade)
print("Altura: ",altura)'''

print('\n')
print(nome[0], "idade:",idade[0],"altura:",altura[0])
print(nome[1], "idade:",idade[1], "altura:",altura[1])
print(nome[2], "idade:",idade[2], "altura:",altura[2])
print(nome[3], "idade:",idade[3], "altura:",altura[3])
print(nome[4], "idade:",idade[4], "altura:",altura[4])

