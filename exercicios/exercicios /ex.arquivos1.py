'''Crie um programa que leia uma lista de nomes fornecidos pelo usuário e salve esta lista no arquivo
‘nomes.txt’. Os nomes são lidos até o usuário fornecer uma string vazia para um dos nomes'''

lista_nomes = []

while True:
    nomes = input('Dígite o nome: ')
    lista_nomes.append(nomes)
    
    continuar = input('Adicionar mais nomes? (s/n): ').lower()
    if continuar != 's':
        break

print('\nLista de nomes: ') 
print(lista_nomes)