'''Faça um Programa que peça as quatro notas de 10 alunos, armazene em uma lista e calcule a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

medias = []
alunos_aprovados = 0

NUMERO_ALUNOS = 2
NUMERO_NOTAS = 4
MEDIA_APROVACAO = 7.0

print("-" * 50)
print(f"Calculadora de Médias para {NUMERO_ALUNOS} alunos")
print("-" * 50)

for i in range(NUMERO_ALUNOS):
    print(f"\n--- Aluno {i + 1} ---")
    soma_notas = 0.0
    
    # Loop interno para solicitar as 4 notas de cada aluno
    for j in range(NUMERO_NOTAS):
        nota = float(input(f"Digite a nota {j + 1} (0 a 10) do Aluno {i + 1}: "))
        soma_notas += nota
    
    media = soma_notas / NUMERO_NOTAS
    medias.append(media)
    print(f"Média calculada para o Aluno {i + 1}: {media:.2f}")

    if media >= MEDIA_APROVACAO:
        alunos_aprovados += 1

print("\n" + "-" * 50)
print("RESULTADOS FINAIS")
print("-" * 50)

print(f"\nLista de médias de todos os {NUMERO_ALUNOS} alunos:")
print([f"{m:.2f}" for m in medias])

# Imprime o número de alunos aprovados
print(f"\nNúmero de alunos aprovados: {alunos_aprovados}")
print("-" * 50)