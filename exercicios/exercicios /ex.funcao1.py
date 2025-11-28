#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses
#três argumentos.

def somar(a, b, c):
    return a + b + c


valor1 = float(input('Digite o primeiro número: '))
valor2 = float(input('Digite o segundo número: '))
valor3 = float(input('Digite o terceiro número: '))


resultado = somar(valor1, valor2, valor3)


print(f'\nA soma dos valores é: {resultado}')
