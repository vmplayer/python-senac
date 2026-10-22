idade = int(input("Digite a idade: "))
matricula = input("Aluno é matriculado [Sim/Não]: ").lower()
autorizacao = input("Possui autorização [Sim/Não]: ").lower()
laboratorio_disponivel = input("Laboratório disponível? [Sim/Não]: ").lower()

if idade >= 16 and laboratorio_disponivel == "sim":
    if matricula == "sim" or autorizacao == "sim":
        print("O acesso está permitido.")
    else:
        print("Acesso negado.")
else:
    print("Acesso negado.")
