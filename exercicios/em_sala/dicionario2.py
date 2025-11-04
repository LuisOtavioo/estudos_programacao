#produto e quantidade em estoque
produto = {'teclado'    : {'quantidade' : 20},
            'monitor'   : {'quantidade' : 10},
            'mouse'     : {'quantidade' : 40},
            'impressora': {'quantidade' : 5}
            }
print(produto)

#acessos
print('Teclado: ', produto['teclado']['quantidade'])
print('Impressora: ', produto['impressora']['quantidade'])

#chegaram 3 mouses
print('\n#### novas impressoras')
produto['impressora']['quantidade'] += 3
print('Impressora agora: ', produto['impressora']['quantidade'])

print('\n#### procurando produto')
procura = input ('digite o nome do produto: ')
if procura in produto:
    print(f'Temos {produto[procura]["quantidade"]} unidades de {procura} em estoque')

print('\n#### percorrendo o dicionário')
for p,q in produto.items():
    print(p, ' Temos: ', q['quantidade'])