def fatorial(n):
	if n == 0:
		return 1 #condição de parada
	else: 
		prod = n*fatorial(n-1)
	return prod

num = int(input('Dígite um número: \n'))
fat = fatorial(num)
print(f'fatorial {num} = {fat}')
