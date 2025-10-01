#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
#seja inválido e continue pedindo até que o usuário informe um valor válido.

print("AVALIAÇÃO DE ATENDIMENTO")
while True:  
    try:
        nota = int(input("Avalie nosso atendimento de 0 à 10: "))
        
        if 0 <= nota <= 10:  # Verifica se a nota está entre 0 e 10
            break  # Sai do loop se a nota for válida
        else:
            print("Nota inválida! Digite um número entre 0 e 10.")
    
    except ValueError:  # Se o usuário digitar algo que não é número
        print("Por favor, digite apenas números!")

if nota in range (5,11):
    print("Agrdecemos a preferencia!")
    print("=" * 50)
    exit()
elif (0 < nota < 5):
    print("Lamentamos não ter atendido suas expectativas.")
    melhoria = input("Gostaria de adicionar um comentário para a melhoria do antendimento? (S/N) \n").upper()
    
if melhoria == 'S': 
    comentario = input("Adicione seu comentário: \n")
    print("Vamos melhorar!")
else:
    print("Agrdecemos a preferencia.")