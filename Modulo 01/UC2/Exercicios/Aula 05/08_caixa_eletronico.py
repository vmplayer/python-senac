saldo = 500.00
saques = 0
depositos = 0

while True:
    print()
    print("=== CAIXA ELETRÔNICO ===")
    print("[1] - Consultar saldo")
    print("[2] - Depositar dinheiro")
    print("[3] - Sacar dinheiro")
    print("[0] - Sair")
    print(f"Saques: {saques}")
    print(f"Depósitos: {depositos}")
    opcao = int(input(""))
    print()

    if opcao == 1:
        print(f"Saldo: R${saldo:.2f
        }")
    
    elif opcao == 2:
        guardar = float(input("Quanto você quer guardar: "))

        saldo += guardar
        depositos += 1

    elif opcao == 3:
        sacar = float(input("Quanto você quer sacar: "))

        if sacar <= saldo:
            saldo -= sacar
            print(f"Você sacou R${sacar:.2f} reais!")
            saques += 1
        else:
            print("Você não tem saldo suficiente para isto!")

    elif opcao == 0:
        print("Saindo do sistema...")
        break
