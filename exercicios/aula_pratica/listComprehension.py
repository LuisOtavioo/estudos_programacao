x2 = list() #cria uma lista vazia
for i in range(6): #i como 0,1,2,3,4,5
	i2 = i*i
	x2.append(i2) #anexa valor i2 na lista x2

print('Lista de quadrados: ')
print(x2)

print('*'*6)

#criando a mesma lista usando List Comprehension
x2 = [i*i for i in range(6)]

print('Lista de quadrados com List Comprehension')
print(x2)
