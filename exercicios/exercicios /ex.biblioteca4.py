'''Glossário 2: Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do
Exercício 3 (Glossário), substituindo sua sequência de instruções print por um laço que percorra as
chaves e os valores do dicionário. 
Quando tiver certeza de que seu laço funciona, acrescente mais cincotermos de Python ao seu glossário.
Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na saída.'''


glossario = {"sorted": "sorted(): retorna a lista ordenada sem alterar a lista original",
            "sort": "sort(): altera a lista para ordem crescente ou alfabética (se for de strings)",
            "replace": "replace: subistitui",
            "append": "append: acrescentar",
            "len": "len(): vem de 'length' que siguinifica 'comprimento'",
            "zip": "zip: Agrupa",
            "extend": "extemd: estender",
            "pop": "pelo índice", 
            "remove": "pelo nome",
            "index": "indica posição",
            "split":  "dividir uma string",
            "set": "evita dados repetidos",
}
dicionario = ("sorted, sort, replace, append, len, zip, extend")


print("---Termos disponiveis---")
print(dicionario)

busca = input('\nDigite o nome do termo: ')

resposta = glossario.get(busca,'palavra não encontrada')
print(resposta)