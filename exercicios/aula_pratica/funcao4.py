#função que imprime a soma de dois números
def soma(x,y):
	#definindo total como a mesma variável
	#em todo o program e funções
	
	global total
	total = x+y #total é local da função
	print("Total soma = ", total)

#__________________________________________
#PROGRAMA PRINCIPAL
global total #total é global do programa principal
total = 10
soma(3,5)
print("Total principal = ",total)

#Observe que total de função soma e do 
#programa principal são os mesmos.
