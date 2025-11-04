produtos = ['tv', 'celular', 'mouse','teclado','tablet']
venda = [1000, 1500, 150, 270, 900]
precoMedio = [2100.00,1780.99,52.45,80.45,1765.32]


#p assume os elementos da lista produtos
#i assume os indices da lista
#no primeiro item da lista i = 0
for i, p in enumerate(produtos):
    print('\n-------------------\n')
    print("produto: ", i)
    print("Tipo: "+ p) 
    print("Vendidos: ", venda[i], "unidades")
    print(f"Preço Médio: R$ {precoMedio[i]:.2f}")
    estimado = venda[i] * precoMedio[i]
    print(f"Valor Estimado: R$ {estimado:.2f}")
    