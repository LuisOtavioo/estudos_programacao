#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
#seja inválido e continue pedindo até que o usuário informe um valor válido.

print("AVALIAÇÃO DE ATENDIMENTO")

while True:  
    nota = int(input("Avalie nosso atendimento de 0 à 10: "))
    
    if 0 <= nota <= 10:  
        break  
    else:
        print("Nota inválida! Digite um número entre 0 e 10.")


# Feedback 

# 1. Notas de 5 a 10 (Satisfeito)
if nota >= 5 and nota <= 10:
    print("Agradecemos a preferência!")
    print("=" * 50)

# 2. Notas de 1 a 4 (Insatisfeito)
elif nota > 0 and nota < 5:
    print("Lamentamos não ter atendido suas expectativas.")
    
    # Coleta de feedback (não precisa de loop, pois aceitamos qualquer entrada)
    melhoria = input("Gostaria de adicionar um comentário para a melhoria do atendimento? (S/N) ").upper()
    
    if melhoria == 'S': 
        comentario = input("Adicione seu comentário: \n")
        print("Agradecemos o seu feedback! Vamos melhorar!")
    else:
        print("Agradecemos a preferência.")


