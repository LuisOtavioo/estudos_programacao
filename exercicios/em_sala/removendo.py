frutas = ['banana', 'mamão','abacaxi','maça','limão','acerola','mamão']

print('lista de frutas: ',frutas)

'''
REMOMVENDO PELO INDICE
remove o 3 elemento da lista pelo índice (abacaxi)
lembrando que o primeiro índice é 0.
portanto o 3. elemento equivale ao índice 2
'''
frutas.pop(2)
print('lista de frutas: ', frutas)

#removendo pelo nome
frutas.remove('mamão')
print('lista de frutas: ', frutas)
#observe que se houver repetidos, somente o primeiro item é removido
