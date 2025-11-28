'''Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. 
Um par chave-valor poderia ser 'Brasil': 'Amazonas'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo: O Amazonas corre pelo Brasil.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.'''


rios = {"Brasil": "Rio Amazonas", 
        "Africa": "Rio Nilo",
        "Asia": "Rio Eufrates",
        }

print('---PAÍSES E SEUS RIOS---')
print("Brasil, Africa, Asia")

busca = input('Dígite o nome do país: ').capitalize()

resposta = rios.get(busca,'paravra não encontrada')
print(resposta)
if resposta == "Brasil":
    print("O Rio Amazonas corre pelo Brasil e é muito lindo")
elif resposta == "Africa":
    print("O Rio Nilo foi muito importante no desenvolver da nossa historia")
elif resposta == "Ásia":
    print("O rio Eufrates junto com Rio Tigres foi muito importante na historia egípcia") 