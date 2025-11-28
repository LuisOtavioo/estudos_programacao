email = 'ptolomeu@alexandria.com.br'

emailSeparado = email.split('@')
print(emailSeparado)

#primeiro elemento de emailSeparado
login = emailSeparado[0]
print("usuario : "+login)

#dividindo o segundo elemento de emailSeparado pelo separador . 
dominio = emailSeparado[1].split('.')

#primeiro elemento de dominio
instituiao = dominio[0]
print("em : "+instituiao)

