'''
Função que incrementa um valor de acordo com o juros dado como entrada 
da função. Se o juros nçao for colocadom supõe-se 10%
'''

def recalculaPreco(valor, taxa=10):
	novoValor = valor + valor*(taxa/100.)
	return novoValor
	
#________________________________________
#PROGRAMA PRINCIPAL
preco = float(input('Digite o preço: '))

#acionando a função somente com preço (aumento de 10%)
novoPreco = recalculaPreco(preco)

print('Novo preço aumentado em 10%: ')
print(f'R${novoPreco:.2f}')
print('\n----\n')

preco = float(input('Digite outro preço: '))
aumento = float(input('Dígite o aumento percentual: '))

#acionando a função somente com preço e taxa
novoPreco = recalculaPreco(preco,aumento)
print(f'Novo preço aumentado em {aumento}%: ')
print(f'R${novoPreco:.2f}')
