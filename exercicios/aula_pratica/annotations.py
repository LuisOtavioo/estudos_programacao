def compra_desconto(idade : int, preco_unitario : float, quantidade : int) -> float:
	#type hint (→ float) que indica o tipo retornado,
	""" retorna o total de uma compra, multiplicando o preço do produto 
	pela quantidade de produtos comprados. Caso o cliente tenha mais de 60 anos
	o total da compra retornado é reduzido em 10%"""
	
	total = preco_unitario*quantidade
	if idade>= 65:
		return 0.9 * total
	else:
		return total

idade = 70
preco = 50
quant = 3
total_pagar = compra_desconto(idade,preco,quant)

print(f'O total a pagar = {total_pagar:.2f}')
