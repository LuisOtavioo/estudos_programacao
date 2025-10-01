#Faça um Programa que solicite uma media em metros com float e mostre o valor desta mediada
#em centímetros.

x = float(input("Dígite a medida em metros: \n"))

#Converte para centímetros (1 metro = 100 centímetros)
centimetros = x * 100

#Resultado
print(f"{x} metros equivalem a {centimetros} centímetros.")