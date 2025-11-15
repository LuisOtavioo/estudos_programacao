def soma(a : int|float, b: int|float) -> int | float:
	""" Esta função realiza a soma de 
	2 números dados na entrada da função
	"""
	
	soma = a + b 
	return soma

s = soma(1,2)
print(s)

''' Recomendável: usar somente type hints como annotations, que indicam o tipo das
variáveis de entrada e o tipo de retorno. '''
