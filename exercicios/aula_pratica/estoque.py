#produto e quantidade em estoque
produto = {'teclado' : 20, 'monitor' : 10 , 'mouse' : 40, 'impressora' : 5}

print('\n#### produto / estoque')
print(produto)

#vendi 4 teclado
produto['teclado'] = produto['teclado'] - 4
print('\n#### produto / estoque depois da venda')
print(produto)

#chegaram 5 monitores
produto['monitor'] = produto['monitor'] + 5
print('\n#### produto / estoque depois da compra')
print(produto)

#quantos mouses eu tenho em estoque?
print('\n#### mouses')
print('tem em estoque: ', produto['mouse'], ' mouses')

#copia um dicionario para o outro - copy()
print('\n#### modei de loja')
produtoNovaLoja = produto.copy()
print('Produto nova loja')
print(produtoNovaLoja)

#apagando os dados da loja antiga - clear()
print('\n#### limpando dados da loja antiga')
produto.clear()
print(produto)
