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

print("Dados do arquivo: ")
for linha in arq:
	print(linha,end='')
	
arq.close()



