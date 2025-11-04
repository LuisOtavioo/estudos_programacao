#criando um dicionario vazio
aula = {}
#adicionando itens ao carro
aula['Segunda'] = 'Programação'
aula['Terça'] = 'Cálculo'
aula['Quarta'] = 'Álgebra'
aula.update({'Quinta' : 'Geometria'})
dia = input('Digite o dia: ')
meteria = input('Dígite a matéria: ')
aula.update({dia : meteria})

print('\n#### horário')
print(aula)

#percorrendo o dicionário pelas chaves
print('\n#### dias de aula')
for dias in aula.keys():
	print('Tenho aula na ' + dias, end = ' - ')
	
#percorrendo o dicionário pelo conteúdo das chaves
print('\n#### materias')
for materia in aula.values():
	print('Tenho aula de '+ materia, end = ' - ')

#percorrendo o dicionario pela chave e conteudo
print('\n#### dias de aula e matérias')
for dias,materias in aula.items():
	print("Aula de ",materias," na ",dias)

#busca do dia de uma matéria 
print('\n#### busca do horário')
materia = input('Digite a matéria: ')
for dias,materias in aula.items():
	if (materias == materia):
		print("Tenho aula de ",materia," na ",dias)
		
