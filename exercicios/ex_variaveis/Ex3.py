#Faça um Programa que peça as 4 notas bimestrais como floats e mostre a média das notas
print("Vamos descorbrir sua média!")

x = float(input("Digite a primeira nota: \n"))
y = float(input("Digite a segunda nota: \n"))
z = float(input("Digite a terceira nota: \n"))
p = float(input("Digite a quarta nota: \n"))

#tira a média
o = x + y + z + p
k = o/2

#Resultado
print(f"Sua média foi de: {k}")