from math import sqrt #função raiz quadradada

def areaQuadrado(lado):
	area = lado*lado
	return area
	
def perimetroQuadrado(lado):
	perimetro = lado+lado+lado+lado
	return perimetro

def diagonalQuadrado(lado):
	diagonal = sqrt(lado**2 + lado**2)
	return diagonal
	
lQ = float(input('Digite o lado do quadrado: \n'))
aQ = areaQuadrado(lQ)
print('A área deste quadrado é: ',aQ)
pQ = perimetroQuadrado(lQ)
print('O perímetro deste quadrado é: ', pQ)
dQ = diagonalQuadrado(lQ)
print('A diagonal deste quadrado é: ', dQ)
