x2Par = list() #cria uma lista vazia
for i in range(6): #i como 0,1,2,3,4,5,
	i2 =i*i 		#i1 -> 0,1,4,9,16,25
	if i%2==0: #anexa valor i2 na lista x2Par
				#somende se i for par
		x2Par.append(i2)
		
print('Lista de quadros de npumeros Pares: ')
print(x2Par)

print('-'*10)

#criando a mesma lista usando List Comprehension
x2Par - [i*i for i in range(6) if i%2 == 0]

print('Lista de quadrados de números pares com List Comprehension')
print(x2Par)
