matrizA = [[1, 5, 6] , [4, 6, 7] , [8, 10, 2] ]

print('Matriz A')
for linha in matrizA:
	print(linha)

matrizB = []

for linha in range(3):
	novaLinha = []
	for coluna in range(3):
		print(f'Digite o elemento ({linha+1},{coluna+1}) para a matriz B: ', end = ' ')
		numero = float(input())
		novaLinha.append(numero)
	matrizB.append(novaLinha)

for linha in matrizB:
	print(linha)
	
