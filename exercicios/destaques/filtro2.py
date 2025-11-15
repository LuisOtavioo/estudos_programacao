import numpy as np
import matplotlib.pyplot as plt

#construindo uma lista x com 10000 elementos
#entre -4 e 4 igualmente espaçados
x = np.linspace(-4,4,10000)

#construindo uma lista y aplicando:
#x^3 -3x +9 da lista x
y = np.power(x,3) -9*x +3


#Criando uma lista com:
# '+' onde y é positivo (>0)
# '-' onde y é negativo (<=0)
sinal = np.where(y>0,'+','-')


#se y passa de menos pra mais 
#ou de mais pra menos   -> temos uma raiz (y~0)
for i in range(len(sinal)-1):
	if (sinal[i] != sinal[i+1]): #se houve mudança de sinal
		print('Raiz em x = ',x[i])
		
print('\n------------\n')

#maximos e minimo global
yMax = y.max()
yMin = y.min()

#localizando x no mácimo e mínimo global
xMax = x[y == yMax]
xMin = x[y == yMin]

print(f'Máximo global em x = {xMax} e y = {yMax}')
print(f'Máximo global em x = {xMin} e y = {yMin}')
print('\n------------\n')

'''
Criando uma lista em que:
- y é crescente: y[i] < y[i+1]
- y é decrescente: y[i] > y[i+1]
'''
estado = []
for i in range(len(y)-1):
	if y[i] < y [i+1]:
		estado.append('C')
	else:
		estado.append('D')

#Se y passou de crescente para decrescente -> máximo local
#Se y passou de descrescente para cresctente -> mínimo local
for i in range(len(estado)-1):
	if (estado[i]=='C' and estado[i+1]=='D'):
		print(f'Máximo local em x = {x[i]} e y{y[i]}')
	elif (estado[i]=='D' and estado[i+1]=='C'):
		print(f'Mínimo local em x = {x[i]} e y = {y[i]}')
print('\n------------\n')



#INTEGRAL
#criando limites para o cálculo da integração
LimInf = -4
LimSup = -1

#filtrando a lista de x e y dentro do limite pedido
xInte = x[(LimInf<x) & (x<LimSup)]
yInte = y[(LimInf<x) & (x<LimSup)]



#calculando a integral pela soma de trapézios
#SOMA DE REIMANN
integralN = np.trapezoid(yInte,xInte)    #`trapz` is deprecated. Use `trapezoid` instead
print(f'Integral numérica entre {LimInf} e {LimSup} = {integralN}')

#integral analítica
integralA = ((1/4*np.power(LimSup,4) - 9/2*np.power(LimSup,2) +3*LimSup)
			-((1/4*np.power(LimInf,4) - 9/2*np.power(LimInf,2) +3*LimInf)))
print(f'Integral analítica entre {LimInf} e {LimSup} = {integralA}')