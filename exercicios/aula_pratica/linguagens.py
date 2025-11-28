#A função set() evita dados repetidos
linguagens_favoritas = {'Jen': 'Python',
						'Sarah': 'C',
						'Edward': 'Java',
						'Phil': 'Python',
					}
print("As seguintes linguagens de programação foram mencionadas: ")
for linguagem in linguagens_favoritas.values():
	print(linguagem)
	
print('\n---- Sem repetição \n')
#set evita repetição
for l in set(linguagens_favoritas.values()):
	print(l)
