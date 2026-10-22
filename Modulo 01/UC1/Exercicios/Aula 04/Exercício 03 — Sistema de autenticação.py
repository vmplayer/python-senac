usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Email: ")
senha = input("Senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado!")
