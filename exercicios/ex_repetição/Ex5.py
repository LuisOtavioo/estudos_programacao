#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print("Eleições")
eleitores = int(input("Qual a quantidade total de eleitores? \n")) #total de eleitores
contagem = 0
c1 = 0 #candidato1
c2 = 0 #candidato2
c3 = 0 #candidato3

print("************")

#enquanto a contagem for menor que o numero de candidatos, o programa continuará rodando 
#isso permite que todos os eleitores façam seu voto, se total de eleitores = 5 o loop rodara 5 vezes.
while (contagem < eleitores):
	contagem += 1
	print("Candidatos para eleição:")
	print("Para candidato 1 vote -> c1")
	print("Para candidato 2 vote -> c2")
	print("Para candidato 3 vote -> c3")
	print("\n  \n")			
	voto = input("Vote no seu candidato: \n")
	if (voto == 'c1'):
		c1 + 1
	elif (voto == 'c2'):
		c2 + 1
	else:
		c3 + 1

	
	print("\n \n")
	print(f"TOTAL DE VOTOS")
	print(f"candidato c1: {c1}")
	print(f"candidato c2: {c2}")
	print(f"candidato c3: {c3}")
	print("\n \n")

	if (c2 < c1 and c3 < c1):
		print(f"O ganhador foi {c1}")
		print("Parabéns!!!")
	elif (c1 < c2 and c3 < c2):
		print(f"O ganhador foi {c2}")
		print("Parabéns!!!")
	else:
		print(f"O ganhador foi {c3}")
		print("Parabéns!!!")

	print("___________________")
	print("fim da votação")

	break