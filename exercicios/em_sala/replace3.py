#lendo um preço como string
precoString = input('Digite o preço unitário (Usar vírgula para separação decimal): \n')
qtd = int(input('Digite a quantidade comprada: \n'))

#trocando o deimal de ',' para '.'
precoString = precoString.replace(',','.')

#fazendo a troca, podemos converter para número
precoFloat = float(precoString) 

#como número, podemos fazer operações arítméticas
total = qtd * precoFloat
print("\nTotal padrão Python", total)

#transformando em total com string com 2 casas decimais
totalString = f'{total:.2f}'

#como string podemos trocar o simbolo decimal
totalString = totalString.replace('.',',')
print("\nTotal (Padrão Brasil) = R$"+totalString)
