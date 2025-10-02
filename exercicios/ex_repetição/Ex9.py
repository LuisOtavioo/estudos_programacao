#Faça um programa que peça 10 números inteiros, calcule e mostre a 
#quantidade de números pares e aquantidade de números impares.


contador = 0

while contador < 10:
	print(f"--- Numero {contador + 1 } de 10 ---")
	numeros = int(input("Digite o número inteiro: "))
	quantidade_numeros = 10
	
	if contador < quantidade_numeros:
		contador += 1
			
	else:
		break
			
print("="*50)
for _ in range (10):
	if (numeros%2 ==0):
		print(f"os numeros pares são: {_}")
	else:
		print(f"os numeros impares são: {_}")