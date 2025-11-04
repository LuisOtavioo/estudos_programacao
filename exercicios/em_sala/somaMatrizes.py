A = [[1, 5, 6] , [4, 6, 7] , [8, 10, 2]]
B = [[4, 3, 2] , [8, 2, 9] , [6,  5, 1]]

print('Matriz A:')
for linha in A:
	print(linha)
print('Matriz B:')
for linha in B:
	print(linha)
	
#somando as duas matrizes elemento por elemento
C = []
for linha in range(3):
	linhaSoma = []
	for coluna in range(3):
		soma = A[linha][coluna] + B[linha][coluna]
		linhaSoma.append(soma)
	C.append(linhaSoma)

print('Soma A+B')
for linha in C:
	print(linha)
	
