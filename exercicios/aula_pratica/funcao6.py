#função maior recebe x e y de entrada
#retorna o maior valor
#return sempre encerra a função


def maior(x,y):
	if x>y:
		return (x)
	else:
		return (y)
		
#usando a função maior
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
M = maior(a,b)
print('O maior número é: ',M)

#usando de novo
a = int(input('\nDigite um número: '))
b = int(input('Digite outro número: '))
M = maior(a,b)
print('O maior número é: ',M)
