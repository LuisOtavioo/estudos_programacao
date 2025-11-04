#lista de dicionarios
notas = [{'Tales de Mileto' : 9.}, {'Ptolomeu' : 8.}, {'Pitágoras' : 9.7}, {'Euclides' : 7.5} ]

numeroAlunos = len(notas)
print('Temos ', numeroAlunos, 'alunos')

# cada elemento da lista é um dicionario
for alunos in notas:
    print(alunos.keys())
    print(alunos.values())

# nota e nome do 2 aluno da lista
print('\n----------------------\n')
print(notas[1])

# - nota do 2 aluno da lista
notas[1]['Ptolomeu'] = 10. #alterando a nota do Ptolomeu
print('\n----------------------\n')
print('Nova nota do Ptolomeu: ', notas[1]['Ptolomeu'])

#percorrendo a lista de nomes e notas
print('\n----------------------\n')
for alunos in notas:
    for nome,nota in alunos.items():
        print(nome, ' - ', nota)
