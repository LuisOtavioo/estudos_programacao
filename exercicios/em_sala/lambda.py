#criando uma função usando lambda
'''
b e h são a base e a altura de um retangulo

nome da função: area_retangulo
paramentro de entrada: b e h
return: b*h
'''

area_retangulo = lambda b,h : b*h

#usando a função com base = 4 e altura = 3 
base = 4
altura = 3
area1 = area_retangulo(4,3)

print(f'A área para {base = } e {altura = } é: {area1}')
