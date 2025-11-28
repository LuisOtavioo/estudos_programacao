#função maior recebe X e Y de entrada
def maior(x,y):
	if x>y:
		print(x)
	else:
		print(y)

#usando a função maior
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('O maior número é: ')
maior(a,b)

#usando de novo
print('Vamos de novo: ')
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('O maior número é: ')
maior(a,b)

if a == b:
	print('Abmos os números são iguais.')
