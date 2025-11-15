from math import sqrt #função raiz quadradada

def dadosQuadrado(lado):
	area = lado*lado
	perimetro = lado+lado+lado+lado
	diagonal = sqrt(lado**2 + lado**2)
	#função retorna 3 valores (tupla)
	return area,perimetro,diagonal

	
lQ = float(input('Digite o lado do quadrado: \n'))
aQ, pQ, dQ = dadosQuadrado(lQ)
print('A área deste quadrado é: ',aQ)
print('O perímetro deste quadrado é: ', pQ)
print('A diagonal deste quadrado é: ', dQ)
