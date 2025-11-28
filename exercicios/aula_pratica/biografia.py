biografia = "A tese do estudioso a de que a Terra era o centro do Universo perdurou durante 14 séculos e foi superada com muita resistência. Ptolomeu jurava de pés juntos que a Terra era o centro e a volta dela girava a Lua, Vênus, Mercúrio, Marte, Júpiter, Saturno, além do sol e das estrelas.\nPtolomeu também chegou a conclusão, através dos seus cálculos, que a Terra era redonda, contrariando toda a tradição que afirmava que a terra era plana.\nNascido no Egito, Ptolomeu encantado pelos astros fez uma série de observações astronômicas e era muito reconhecido pelos seus contemporâneos. O estudioso foi tido como o último grande intelectual grego da Antiguidade."

print(biografia)

#dividindo por paragrafo
biografia = biografia.split('\n')
print('\n-----------\n')
print(biografia)
print('\n 1. paragrafo \n')
print(biografia[0])
print('\n 2. paragrafo \n')
print(biografia[1])
print('\n 3. paragrafo \n')
print(biografia[2])
print('\n-----------\n')

#dividindo o ultimo paragrafo por frase
biografia = biografia[-1].split('.')
print('\n 1 frase do último paragrafo\n')
print (biografia[0])
print('\n 2 frase do último paragrafo\n')
print (biografia[1])

#dividindo o último paragrafo em palavras
print('\n-----------\n')
biografia = biografia[1].split(' ')
print('Ultima palavra da última frase')
print(biografia[-1])
