def soma (a, b, c):
	"""
	Esta função realiza a soma de três números inteiros
	ou floats dados na entrada da função.
	
	Parameters:
			a (int | float): O primeiro número.
			b (int | float): O segundo número.
			c (int | float): O terceiro número.
	Returns:
			soma (int | float) : A soma de a, b e c.
	"""
	soma = a + b + c
	return soma
	
	
s = soma(1,2,3)
print(s)
