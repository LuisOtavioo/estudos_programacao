funcionario = ['Newton', 'leibniz', 'Gauss']
salario = [5424.45 , 10323.00 , 2500.00]
anoIngresso = [2015,2020,2017]

for i in range (3): # i de 0 até 2
    print("\n-------------------\n")
    print('Funcionário: ', i+1) #o primeiro i é de 0
    print('Nome: '+funcionario[i])
    print(f'Salário: R$ {salario[i]:.2f}')
    print('Ano de Ingresso: ', anoIngresso[i])  
