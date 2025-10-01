# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print("Eleições")
eleitores = int(input("Qual a quantidade total de eleitores? \n")) #total de eleitores
contagem = 0

A = 0 #candidato1
B = 0 #candidato2
C = 0 #candidato3

#print("************") 
print("\n" * 10) #equivalente

# enquanto a contagem for menor que o numero de candidatos, o programa continuará rodando 

while (contagem < eleitores):
	print(f"\n--- Eleitor {contagem + 1 } de {eleitores}---")
	print("CANDIDATOS PARA ELEIÇÃO:")
	print("Para candidato 1 vote -> A")
	print("Para candidato 2 vote -> B")
	print("Para candidato 3 vote -> C")
	print("\n")			

	voto = input("Vote no seu candidato: \n").upper()

	if (voto == 'A'):
		A += 1
	elif (voto == 'B'):
		B += 1
	elif (voto == 'C'):
		C += 1
	else:
		print("Voto inválido!")
		continue

	contagem += 1
	print("Voto computado com sucesso!")

print("\n" + "="*50)
print("RESULTADO FINAL DA ELEIÇÃO")
print("="*50)
print(f"TOTAL DE VOTOS:")
print(f"candidato 1: {A}")
print(f"candidato 2: {B}")
print(f"candidato 3: {C}")

print("\n" + "="*50)


	# Verificação do ganhador
if (A > B and A > C):
    print(f"\n O ganhador foi o Candidato 1 com {A} votos!")
    print(" Parabéns!!!")
elif (B > A and B > C):
    print(f"\n O ganhador foi o Candidato 2 com {B} votos!")
    print(" Parabéns!!!")
elif (C > A and C > B):
    print(f"\n O ganhador foi o Candidato 3 com {C} votos!")
    print(" Parabéns!!!")
else:
    print("\n Houve um empate!")
    if A == B == C:
        print("Todos os candidatos tiveram a mesma quantidade de votos!")
    elif A == B and A > C:
        print(f"Empate entre Candidato 1 e Candidato 2 com {A} votos cada!")
    elif A == C and A > B:
        print(f"Empate entre Candidato 1 e Candidato 3 com {A} votos cada!")
    elif B == C and B > A:
        print(f"Empate entre Candidato 2 e Candidato 3 com {B} votos cada!")
        
print("\n" + "="*50)
print("FIM DA VOTAÇÃO \n")