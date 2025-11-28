matricula = {1101 : 'Newton', 1102 : 'Laplace', 1103: 'Hipátia'}

print('\n---\n dicionario: ')
print(matricula)

#acessando um elemento pela chave
print('\n---\n acessando: ')
print(matricula[1101])
print(matricula[1103])

#adicionando um novo elemnto pela chave
print('\n---\n adicionando: ')
matricula[1102] = 'Euclides'
print(matricula)

#alterando o conteudo de uma chave
print('\n---\n modificando: ')
matricula[1102] = 'Gauss'
print(matricula)

#removendo - método pop
print('\n---\n removendo chave 1101')
matricula.pop(1101)
print(matricula)

#key informa todas as chaves de um dicionario
print('\n---\n informando as chaves disponiveis: ')
print(matricula.keys())

#key informa o conteudo das chaves de um dicionario
print('\n---\n informando os conteudos disponiveis: ')
print(matricula.values())

#juntando os 2 dicionarios
print('\n---\n juntando: ')
matricula2 = {2101 : 'Leibintz', 2102 : 'Fourier', 2103: 'Bessel'}
matricula.update(matricula2)
print(matricula)
