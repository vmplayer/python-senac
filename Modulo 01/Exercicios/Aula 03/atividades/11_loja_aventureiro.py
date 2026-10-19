aventureiro_nome = input("Digite o nome do aventureiro: ")
aventureiro_ouro = int(input("Digite a quantidade de ouro do aventureiro: "))

if aventureiro_ouro < 0:
    print("Quantidade de ouro inválida.")
else:
    print("       === MENU ===")
    print("[1] - Poção de vida (25 moedas)")
    print("[2] - Escudo (60 moedas)")
    print("[3] - Espada (100 moedas)")
    print()
    opcao = input("Selecione uma opção: ")

    if opcao != "1" and opcao != "2" and opcao != "3":
        print("Opção inválida!")
    else: 
        if opcao == "1":
            if aventureiro_ouro < 25:
                print("Você ainda não pode comprar isso.")
                print(f"Faltam: {25 - aventureiro_ouro}.")
            else:
                aventureiro_ouro -= 25
                print("Você comprou: Poção de vida!")
                print(f"Ouro restante: {aventureiro_ouro}.")
        elif opcao == "2":
            if aventureiro_ouro < 60:
                print("Você ainda não pode comprar isso.")
                print(f"Faltam: {60 - aventureiro_ouro}.")
            else:
                aventureiro_ouro -= 60
                print("Você comprou: Escudo!")
                print(f"Ouro restante: {aventureiro_ouro}.")
        elif opcao == "3":
            if aventureiro_ouro < 100:
                print("Você ainda não pode comprar isso.")
                print(f"Faltam: {100 - aventureiro_ouro}.")
            else:
                aventureiro_ouro -= 100
                print("Você comprou: Espada!")
                print(f"Ouro restante: {aventureiro_ouro}.")
