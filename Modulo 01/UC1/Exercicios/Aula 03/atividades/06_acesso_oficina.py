idade = int(input("Digite a sua idade: "))

if idade < 0 or idade > 112:
    print("Idade inválida.")
else: 
    inscricao = input("Possui inscrição? [sim/nao] ").lower()

    if inscricao != "sim" and inscricao != "nao":
        print("O valor digitado não existe.")
    else:
        if idade < 14 and inscricao == "nao":
            print("Você precisa ter idade o suficiente e ter uma inscrição.\nNenhum requisito foi atendido.")
        elif inscricao == "nao":
            print("Você precisa ter feito sua inscrição. Sua entrada é proibida.")
        elif idade < 14:
            print("Você não tem idade o suficiente para participar.")
        else:
            print("Entrada permitida!")
