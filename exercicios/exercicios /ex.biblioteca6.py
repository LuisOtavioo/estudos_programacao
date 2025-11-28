'''Enquete: Utilizando o código abaixo:
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns
nomes que já estejam no dicionário e outros que não estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete,
mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da
enquete,apresente uma mensagem convidando-as a responder.'''

linguagens_favoritas = {'Jen': 'Python',
                        'Sarah': 'C',
                        'Edward': 'Java',
                        'Phil': 'Python',
                        }

print('As seguintes linguagens de programação foram mencionas: ')
for linguagem in linguagens_favoritas.values():
    print(linguagem)

print('\n--- Sem repetição ---')
#set evia repetições
for linguagem in set(linguagens_favoritas.values()):
    print(linguagem)