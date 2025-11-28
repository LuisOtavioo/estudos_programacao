'''Faça um programa que leia o nome para um arquivo, verifique se o arquivo existe, caso não exista
encerre o programa. Caso exiba as informações do arquivo na tela e pergunte ao usuário se ele deseja
anexar outras informações. Caso deseje leia as informações do usuário e anexe ao arquivo. Exiba
nova'''

import os 

nome_arquivo = 'arquivo.txt'

if os.path.exists(nome_arquivo):
    if os.path.isfile(nome_arquivo):
        print(f" O arquivo '{nome_arquivo}' existe!")
    else:
        exit()


while True:
    adicionar = input('Deseja anexar informações?(s/n)').lower()

    if adicionar == 's':
        novo_dado = input("Por favor, digite o dado que deseja adicionar ao arquivo: ")
    
    else:
        break


    with open("arquivo.txt","w") as f:
        f.write(novo_dado + "\n")

    print("\n---arquivo.txt ---")
    with open("arquivo.txt", "r") as f:
        conteudo = f.read()
        print(conteudo)