print("Escolha uma opção: ")
print("1 - água")
print("2 - café")
print("3 - chá")
print("4 - refrigerante")
print("5 - suco")

opcao = int(input("Opção: "))

print("\n###############\n")

if (opcao == 1):
    print("Servindo água")
elif (opcao == 2):
    print("Servindo café ")
elif (opcao == 3):
    print("Servindo chá ")
elif (opcao == 4):
    print("Servindo refrigerante ")
elif (opcao == 5):
    print("Servindo suco ")
else:
    print("opção inválida")