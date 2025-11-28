import numpy as np

#criando um array entre -2pi e 2pi com 1000 pontos
x = np.linspace(-2*np.pi,2*np.pi,1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

#salvando dados linha por linha
#arquivo csv -> dados separados por ;

print('Salvando dados')
with open('tabela.csv','w') as arq:
	for lx,ly1,ly2,ly3 in zip(x,y1,y2,y3):
		
		#convertendo dados para string
		linha = f'{lx};{ly1};{ly2};{ly3}\n'
		
		#salvando dados separados por ;
		arq.write(linha)

print('Dados Salvos.')
#verifique o arquivo tabela.csv no excel
