#Lendo o arquivo linha por linha

import os.path, sys

nome = 'meuArquivo.txt'

#verifica se o meuArquivo.txt existe
if(os.path.exists(nome)):
	print("O meuArquivo.txt existe")
	print('\n-----------\n')
else:
	sys.exit('Arquivo não existe, encerrando...')

#abrindo 'meuArquivo.txt' em modo leitura
arq = open('meuArquivo.txt','r')


print("Dados do arquivo: ") #le primeira linha
linha = arq.readline()

while(linha): #le enquanto houver conteudo na linha
	print(linha,end= '')
	linha = arq.readline()

arq.close()
