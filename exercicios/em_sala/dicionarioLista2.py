#produtos como lista
# ~ listaProdutos = [ 'teclado', 'mouse', 'monitor', 'impressora' ],
# ~ 				  [ 'Logic'  , 'PosM' , 'Lg'     , 'HP'			],
# ~ 				  [   20 	 ,   40  ,	10	   ,
# ~ 				  [ 50.20   , 45.00 , 1500.00 , 2543.21    ]

#produtos como dicionario e lista
listaProdutos = { 'teclado' : {'marca' : 'Logic' , 'estoque' : 20 , 'preço' : 50.20 }, 
                    'mouse' : {'marca' : 'PosM' , 'estoque' : 40 , 'preço' : 45.00 },
                    'monitor' : {'marca' : 'Lg' , 'estoque' : 10 , 'preço' : 1500.00 },
                    'impressora' : {'marca' : 'HP' , 'estoque' : 5 , 'preço' : 2543.21 },
                }

numTeclados = listaProdutos['teclado']['estoque']
print('Temos ', numTeclados, ' teclados')

print('\n### lista de produtos')
for prod,dados in listaProdutos.items():
    print('Produto: '+prod)
    print('Marca: ',dados['marca'])
    print('Estoque: ',dados['estoque'])
    print('Preço: ',dados['preço'])
    print('\n----------------\n')

print('\n---------------\n')
print('\n BUSCA \n')
busca = input('Digite o nome do produto: ')
if busca in listaProdutos.keys():
    print('Produto: '+busca)
    print('Marca: ',listaProdutos[busca]['marca'])
    print('Estoque: ',listaProdutos[busca]['estoque'])
    print('Preço: ',listaProdutos[busca]['preço']) 
