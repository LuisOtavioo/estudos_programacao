def checar_aprovacao(nome : str, notas : list[float]) -> tuple[float,bool]:
	""" 
	Calcula a média da lista notas.
		Se a média for >= 5 retorna média e aprovação (True)
		Se a média for < 5 retorna média e reprovação (False)
		
	Parameters:
		nome (str): nome do aluno
		notas (list): lista de notas do aluno
	
	Returns:
		media (float): média do aluno
		aprovacao (bool): True se aprovado ou False se reprovado
	"""
	
	media = sum(notas)/len(notas)
	if media >= 5:
		return media,True
	else:
		return media,False
		
nome = 'Platão'
provas = [3,4,5,6]
nota_final , aprovado = checar_aprovacao(nome,provas)

if aprovado:
	print(f'{nome} aprovado com média de {nota_final}')
else:
	print(f'{nome} reprovado. Média de {nota_final}')
