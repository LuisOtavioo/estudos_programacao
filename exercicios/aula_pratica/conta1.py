agSistema = '9999-9'
contasSistema = '8888-8'
senhaSistema = 7777

ag_Usuario = input("Dígite sua agência: \n")
conta_Usuario = input("Dígite seu usuário: \n")
senha_Usuario = int(input("Por favor, dígite sua senha: \n"))


if (agSistema == ag_Usuario):
    if(contasSistema == conta_Usuario):
        if(senhaSistema == senha_Usuario):
            print("=" * 50)
            print("Acesso liberado!")
            print("=" * 50)
        else:
            print("=" * 50)
            print("dados incorretos")
            print("Acesso negado")
            print("=" * 50)
            
    else:
        print("=" * 50)
        print("dados incorretos")
        print("Acesso negado")
        print("=" * 50)
else:
    print("=" * 50)
    print("dados incorretos")
    print("Acesso negado")
    print("=" * 50)