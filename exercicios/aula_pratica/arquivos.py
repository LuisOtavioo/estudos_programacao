#Gravando dados em um novo arquivo

import os.path

#abrindo 'meuArquivo.txt' em modo escrita
arq = open('meuArquivo.txt','w')

mens1 = 'Arquimedes de Siracursa\n'
mens2 = 'Pitágoras de Samos \n'
mens3 = 'Euclides de Alexandria'

#gravando dados no meuArquivo.txt
arq.write(mens1)
arq.write(mens2)
arq.write(mens3)

#fechando meuArquivo.txt
arq.close()

#verifica se o meuArquivo.txt existe
if(os.path.exists('meuArquivo.txt')):
	print("O meuArquivo.txt existe")
else:
	print("O meuArquivo.txt não existe.")
