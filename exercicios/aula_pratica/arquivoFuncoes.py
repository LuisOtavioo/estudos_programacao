import os.path, sys

def imprimirTudo(arq):
	dados = arq.read()
	print(dados)
	
def voltarParaOInicio(arq):
	arq.seek(0)
	
def imprimirUmaLinha(numeroDaLinha,arq):
	linha = arq.readline()
	print(numeroDaLinha,linha)

nome = 'meuArquivo.txt'

#verifica se o meuArquivo.txt existe
if(os.path.exists(nome)):
	print('O arquivo '+ nome+' pode ser acessado')
	print('\n-----------\n')
else:
	sys.exit('Arquivo não existe, encerrando...')


arq = open(nome,'r')

print('Imprimindo todo o arquivo: ')
imprimirTudo(arq)

print('\n---\nRetornando ao inicio do arquivo')
voltarParaOInicio(arq)

print('Imprimindo 3 primeiras linhas')
for l in range(3):
	imprimirUmaLinha(l+1,arq)
	
arq.close()
