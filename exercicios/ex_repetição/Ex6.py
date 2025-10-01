# Faça um programa que leia 5 números e informe a soma e a média dos números.
print("Vamos calcular a soma e média entre 5 números")
a = int(input("Digite o primeiro numero: \n")) #1
b = int(input("Digite o segundo numero: \n")) #2
c = int(input("Digite o terceiro numero: \n")) #3
d = int(input("Digite o quarto numero: \n")) #4
e = int(input("Digite o quinto numero: \n")) #5 

x = a + b + c + d + e 
z = x/5

print("\n" + "="*50)
print(f"A soma dos números informado é igual a {x}")
print(f"Já a média entre elas é de {z} \n ")