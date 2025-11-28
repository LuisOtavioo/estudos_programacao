import os.path, sys
import matplotlib.pyplot as plt

nome = 'tabela.csv'

if(os.path.exists(nome)):
	print('O arquivo '+nome+' existe')
	print('\n-------\n')
else:
	sys.exit('Arquivo não existente, encerrando')

x = []
y1 = []
y2 = []
y3 = []

print('lendo arquivo')
with open('tabela.csv', 'r') as arq:
	for linha in arq:
		dados = linha
		dados.replace('\n','')
		dados = linha.split(';') #separa em lista
		x.append(float(dados[0]))
		y1.append(float(dados[1]))
		y2.append(float(dados[2]))
		y3.append(float(dados[3]))
		
#GRAFICOS
plt.plot(x,y1, label = 'seno(x)'
plt.plot(x,y2, label = 'cosseno(x)')
plt.plot(x,y3, label = 'seno(x) + cosseno(x)')
plt.axhline
plt
plt
plt
plt
plt
plt
plt
plt
plt
plt
