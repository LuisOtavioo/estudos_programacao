#sequencia de listas de produtos disponiveis
produtos = ['teclado','mouse','monitor','impressora']
marca 	 = ['Logic'  ,'PosM' ,'Lg'     ,'HP'		]
estoque  = [  20 	 ,   40  ,	10	   , 5			]
preco 	 = [ 50.20   , 45.00 , 1500.00 , 2543.21    ]

print("produto,  marca, estoque,  preço")
for p,m,e,pr in zip(produtos,marca,estoque,preco):
	print(f'{p:10s} : {m:7s} : {e:3d} : R${pr:.2f}')

listaProdutos = [['teclado','mouse','monitor','impressora'] ,
				 ['Logic'  ,'PosM' ,'Lg'     ,'HP'		  ] ,
				 [  20 	 ,   40  ,	10	   , 5			  ] ,
				 [ 50.20   , 45.00 , 1500.00 , 2543.21    ]]

#acessando a lista
print(listaProdutos[0])
print(listaProdutos[1])
print(listaProdutos[2])
print(listaProdutos[3])

#acessando elementos
print(listaProdutos[0][0])
print(listaProdutos[0][1])
print(listaProdutos[0][2])
print(listaProdutos[0][3])

print('----------------')
print(listaProdutos[1][0])
print(listaProdutos[1][1])
print(listaProdutos[1][2])
print(listaProdutos[1][3])

print('----------------')
print(listaProdutos[2][0])
print(listaProdutos[2][1])
print(listaProdutos[2][2])
print(listaProdutos[2][3])

print('----------------')
print(listaProdutos[3][0])
print(listaProdutos[3][1])
print(listaProdutos[3][2])
print(listaProdutos[3][3])

print('----------------')