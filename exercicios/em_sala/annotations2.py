def soma(a : 'primeiro número int|float', b : 'segundo número int|float') -> 'soma dos números int|float':
	"""
	Esta função realiza a soma de 2 números dados na entrada da função.
	"""
	soma = a + b 
	return soma
	
s = soma(1,2)
print(s)

"""
Não é recomendável, mas pode-se colocar o descritivo do argumento usando annotations.
Neste caso, o mais recomendável seria fazer uma docstring
"""
#Não recomendável
