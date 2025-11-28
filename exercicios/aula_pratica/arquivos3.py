#Anexando dados

import os.path, sys

nome = 'meuArquivo.txt'

if(os.path.exists(nome)): #verifica a existencia do arquivo
	print('O arquivo '+ nome+ ' pode ser acessado')
	print('\n-------\n')
else:
	sys.exit('Arquivo não econtrado/não existe, encerrando...')

arq = open('meuArquivo.txt', 'a') #abrindo em modo anexo

#anexando dados
arq.write('\nTales de Mileto\n')
arq.write('Ptolomeu de Alexandria \n')

arq.close()
