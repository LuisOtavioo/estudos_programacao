'''Faça um programa que leia um nome para um arquivo, anexe ‘.txt’ ao nome dados pelo usuário, e
cria o arquivo com este nome+’.txt’. Como no exercício anterior leia uma sequência de nomes e
salve os nomes lidos neste novo arquivo.'''

novo_dado = input("Por favor, digite o dado que deseja adicionar ao arquivo: ")

with open("arquivo.txt","w") as f:
    f.write(novo_dado + "\n")

print("\n---arquivo.txt ---")
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

