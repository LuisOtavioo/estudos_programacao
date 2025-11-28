def fatorial(n):
	prod = 1 #produtorio n *(n-1) * (n-2) + .....1
	if n == 0:
		return 1
	for i in range(n,0,-1):
		prod = prod * i
	return prod

num = int(input('Digite um número: \n'))
fat = fatorial(num)
print(f'fatorial {num} = {fat}')

