idade = int(input("Dígite sua idade: \n"))
deficiencia = input("Possui alguma deficiência física? (s/n) \n")
gestante = input("Gestante? (s/n) \n")

print("\n###########\n")
if ((idade >=65) or (idade < 12) or (gestante =='s') or (deficiencia =='s')):
    print("Atendimento prioritario")
    atendimento = "especial"
else:
    print("Atendimento normal")
    atendimento = 'normal'
    
print("\n############\n")
print("iniciando atendimento " + atendimento)