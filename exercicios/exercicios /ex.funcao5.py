'''Faça um programa para imprimir a saída abaixo para um n informado pelo usuário. Use uma função
que receba um valor n inteiro e imprima até a n-ésima linha.'''

def imprimir_padrao(n):
 
    for i in range(1, n + 1):
        linha_completa = (str(i) + " ") * i
        
        print(linha_completa[:-1])

n = int(input('Digite o número de linhas (n): '))

imprimir_padrao(n)