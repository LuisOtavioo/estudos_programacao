#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.


while(True):

	pA = int(input("Digite a quantidade de habitantes do pais A: \n"))
	pB = int(input("Digite a quantidade de habitantes do pais B: \n"))
	txA = float(input("Qual a porcentagem de crescimento do pais A?\n"))
	txB = float(input("Qual a porcentagem de crescimento do pais b?\n"))
	ano = 0

	while pA < pB :
		pA = (pA * txA) + pA
		pB = (pB * txB) + pB
		ano += 1
		
	print("\n           \n ")
	print(f"Levara {ano} anos para terem a mesma quantitade de habitantes.")
	repetir = ''
	while (not (repetir == 's' or repetir == 'n')):
		repetir = input("Deseja repetir a simulação? (s/n) \n")
	if (repetir == 's'):
		continue
	else:
		break