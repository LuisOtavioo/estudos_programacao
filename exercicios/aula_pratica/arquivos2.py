#Lendo dados do arquivo

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

#lendo dados do arquivo
dados = arq.read()

print("Dados do arquivo: ")
print(dados)

arq.close() #fechando o arquivo
