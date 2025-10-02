print("Cálculo bônus do mês do vendedor: ")
vCrediado = input("O vendedor é credenciado: (s/n) \n")
tVendas = float(input("Digite o total de vendas do mês em reais: \n"))
qVendas = int(input("Digite a quantidade de vendas no mês: \n"))

if ((vCrediado == 's') and ((tVendas > 1.e3 or qVendas > 100))):
    print("Vendedor com bônus de R$500,00")
else:
    print("Vendedor com bonus de R$100,00")
