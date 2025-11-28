import os.path

#abrindo meuArquivo.txt em modo escrita
nome = 'meuArquivo.txt'

mens1 = 'Arquimedes de Siracusa'
mens2 = 'Pitagoras de Samos'
mens3 = 'Euclides de Alexandria'


#usando with para salvar dados no arquivo
with open(nome,'w') as arq:
	arq.write(mens1+'\n')
	arq.write(mens2+'\n')
	arq.write(mens3+'\n')
	
#usando with para ler dados no arquivo
with open(nome,'r') as arq:
	dados = arq.read()

print('Dados do arquivo: ')
print(dados)
