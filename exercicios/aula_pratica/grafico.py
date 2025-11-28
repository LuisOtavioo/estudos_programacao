import numpy as np
import matplotlib.pyplot as plt

# contruindo uma lista x com 50 elementos
# entre -4 e 4 igualmente espaçados
#sugestão: depois faça testes com 100 e 1000 elementos

x = np.linspace(-4,4,50)

#construindo uma lista y aplicando:
#x^3 -3x +9 da lista x

y = np.power(x,3) -9*x +3

#derivada analítica 
#dy/dx = 3*x^2 -9
dydxAnalitica = 3*x*x -9

#derivada numérica 
# (y[i+1]-y[i])/(x[i+1]-x[i])
dydxNumerico = np.diff(y)/np.diff(x)

'''
graficando y por x
cor: azul
nome: 'x**3 -9*x+3'
estilo de linha: -
espessura da linha = 4
'''
plt.plot(x,y,label='x**3 -9*x+3',color = 'blue',linestyle = '-',linewidth=4)

'''
graficando dy/dx numérico
cor:vermelha
nome: 'x**3 -9*x+3'
estilho de linha: null
marcação em pontos: o
a lista x tem um elemento a mais que dydxNumerico, eliminamos o primeiro valor com x[1:]
'''
plt.plot(x[1:],dydxNumerico,label='dy/dx numerico',color = 'red',linestyle = '',marker = 'o')


'''
graficando dy/dx analitico
cor: verde
nome: 'dy/dx analítico'
estilo de linha: --
espessura da linha = 2
'''

plt.plot(x,dydxAnalitica,label='dy/dx analítico', color = 'green',linestyle = '--',linewidth=2)

#linha vertical preta em y=0
plt.axhline(y=0,color = 'black',linestyle='-')

#titulo do gráfico 
plt.title('Análise de dados')

#nome dos eixos
plt.xlabel('x')
plt.ylabel('y')

#exibir a legenda de cada gráfico
plt.legend()

#exibir linhas de grade
plt.grid()

#salvando gráficos como figura em pdf no disco
plt.savefig('figura.pdf')


#exibindo o grafico
plt.show()
