produtos = ['tv','celular','mouse','teclado','tablet']
venda = [1000, 1500, 15, 270, 900]
precoMedio = [2100.00,1780.99,52.45,80.45,1765.32]

#p assume os elementos da lista produtos
#i assume os indices da lista produtos
#no primeiro item da lista i=0

print("Lista de Produtos: ")
for P,V,Pmedio in zip(produtos,venda,precoMedio):
	print("\n-----------\n")
	print("Tipo: "+ P)
	print("Vendidos: ", V, "unidades")
	print(f"Preço Médio: R${Pmedio:.2f}")
	estimado = V*Pmedio
	print(f"Faturamento médio: R${estimado:.2f}")
	
