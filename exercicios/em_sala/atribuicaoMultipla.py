#múltiplas atribuições

a = b = c = d = 10
print('valores para a,b,c,d')
print(f'{a = } ; {b = }, {c = }, {d = } ')

print('-------------------------')
#Atribuição com desempacotamento
x,y,z = 10, 20, 30
print('Valores para x, y, z')
print(f'{x = } ; {y = }, {z =} ')

print('-------------------------')
k,w = 5,10
print('Valores para k, w')
print(f'{k = } ; {w = }' )

print('-------------------------')
#trocando os valores

k,w = w,k
print('Valores k, w após troca')
print(f'{k = } ; {w = }')