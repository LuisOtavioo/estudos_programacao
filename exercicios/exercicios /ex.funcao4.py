'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o
programa deve converter 14:25 em 2:25 P.M, e retornar a nova hora como string. A entrada é dada
em dois inteiro representando a hora e o minuto. No programa principal, inclua um loop que permita
que o usuário repita esse cálculo para novos valores de entrada'''

#def converter(hora, minuto):
 #   return 


while True:
    print('---conversão de horas---')
    print('Convertendo 23hrs para 12hrs\n')

    hora = int(input('Digite o horário: '))
    minuto = int(input('Dígite os minutos: '))

    match hora:
        case 13:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 14:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 15:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 16:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 17:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 18:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 19:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 20:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 21:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 22:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 23:
            print(f'\nA hora convertida é: {hora - 12}:{minuto} PM\n')
        case 0:
            print(f'\nA hora convertida é: 12:{minuto} AM\n')

    continuar = input('Deseja converter outro horário? (s/n): ')
    if continuar.lower() != 's':
        break
print('\nPrograma encerrado.')

