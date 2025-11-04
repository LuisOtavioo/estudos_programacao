telefones = {'John' : 9876654 , 'Paul' : 9822423 , 'George' : 96111412, 'Richard' : 941423152}

print('\n### listando os nomes')
print(telefones.keys())

print('\n### listando os calores guardados nas chaves')
print(telefones.values())

print('\n### Telefone do Paul: ')
print(telefones['Paul'])

#com o metodo get, teriamos uma mensagem de erro caso não haja a chave na lista
print('\n### busca de contato')
print(telefones.get('Paul', 'Não temos este número'))
print(telefones.get('Martin', 'Não temos este número'))

#busca de valores pela chave
print('\n### busca de contato com if')
busca = input("Digite um nome: ")
if (busca in telefones.keys()):
	print(f'Telefone de {busca} : {telefones[busca]}')
else:
	print('Não temos este número')
	
#busca de valores conteudo
#vamos transformar as chaves e conteudos em lista
listaNomes = list(telefones.keys())
listaNumeros = list(telefones.values())
print('\n### busca de contato com o numero')
busca = int(input('Dígite um numero: '))

if busca in listaNumeros:
	indiceBusca = listaNumeros.index(busca) #procua o indice do numero
	print(f'Telefone de {busca} pertence {listaNomes[indiceBusca]}')
else:
	print('Numero não existe na agenda')
	