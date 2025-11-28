'''Faça um programa com uma função chamada de somaImposto. A função possui dois parâmetros
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 'custo',
que é o custo de um item antes do imposto. A função retorna o valor final do custo para incluindo o
imposto sobre vendas.'''

def somaImposto(taxaImposto, custo):
    return custo + (custo * taxaImposto)

custo = int(input('Dígite o valor da venda:'))
taxaImposto = float(input('Dígite a porcentagem do imposto(ex:0,03): ')) #3% = 0,03

valor_final = somaImposto(taxaImposto, custo)

print(valor_final)