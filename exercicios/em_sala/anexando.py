listaMusica = [] #cira uma lista vazia

while (True):
	nomeMusica = input('Digite a música pedida: \n')
	if (not nomeMusica): #se n houver nada digitado
		break
	#Anexa a música digitada a lista de músicas
	listaMusica.append(nomeMusica)
	
	print("\nTocando: ")
	for playList in listaMusica:
		print(playList)
		
