#função que retorna a soma de dois numeros 
#sem imprimair nada na tela

def soma(x,y):
	total = x+y
	return total
	#Devolve o conteúdo de total onde a função foi criada

#________________________________________
#PROGRAMA PRINCIPAL
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
somaAB = soma(a,b) #recebe o retorno de soma(x,y)
print('A soma dos números é: ',somaAB)
