materialEstoque = ['lápis','borracha','caneta']
print('material disponivel:', materialEstoque)

#ligando as duas listas
listaPedida = materialEstoque[:]

#anexando uma régua na listaPedida
listaPedida.append('régua')

#observe que as duas listas foram alteradas
print('\n-------')
print('lista material pronto: ', materialEstoque)
print('lista pedida: ', listaPedida)

#Ao fazer umaLista = outraLista[], somente os dados de outraLista são copiados para umaLista.
#Qualquer modificação em qualquer lista não altera a outra.
