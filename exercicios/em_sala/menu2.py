print("Escolha uma opção: ")
print("1 - água")
print("2 - café")
print("3 - chá")
print("4 - refrigerante")
print("5 - suco")

opcao = int(input("Opção: "))

print("\n###############\n")

match opcao:
    case 1: print("Servindo água")
    case 2: print("Servindo café")
    case 3: print("Servindo chá")
    case 4: print("Servindo refrigerante")
    case 5: print("Servindo suco")
    case _: print("opção invalida.")
    