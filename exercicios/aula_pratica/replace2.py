nome = input("Digite seu nome: \n")
print("-"*30)

nome = nome.title() # Coloca a primeira letra de cada palavra em maiúsculo
print(nome)

# Ajustando as ligações (observe os espaços em branco)
nome = nome.replace(" De ", " de ")
nome = nome.replace(" Da ", " da ")
nome = nome.replace(" Do ", " do ")
nome = nome.replace(" Das ", " das ")
nome = nome.replace(" Dos ", " dos ")
nome = nome.replace(" E ", " e ")
print("-"*30)