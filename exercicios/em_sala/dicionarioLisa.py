#produtos como lista
# ~ listaProdutos = [ 'teclado', 'mouse', 'monitor', 'impressora' ],
# ~ 				  [ 'Logic'  , 'PosM' , 'Lg'     , 'HP'			],
# ~ 				  [   20 	 ,   40  ,	10	   ,
# ~ 				  [ 50.20   , 45.00 , 1500.00 , 2543.21    ]

#produtos como dicionario e lista
listaProdutos = { 'teclado' : ['Logic', 20 , 50.20 ], 
                    'mouse' : ['PosM' , 40 , 45.00 ],
                    'monitor' : ['Lg' , 10 , 1500.00],
                    'impressora' : ['HP' , 5 , 2543.21],
                }

for prod,listaDados in listaProdutos.items():
    print('Produto: '+prod)
    print('Marca: ',listaDados[0])
    print('Estoque: ',listaDados[1])
    print('Preço: ',listaDados[2])
    print('\n----------------\n')

print('\n BUSCA \n')
busca = input('Digite o nome do produto: ')
if busca in listaProdutos.keys():
    print('Produto: '+busca)
    print('Marca: ',listaProdutos[busca][0])
    print('Estoque: ',listaProdutos[busca][1])
    print('Preço: ',listaProdutos[busca][2])