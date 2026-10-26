while True:
    print()
    print("=== MENU ===")
    print("[1] - Somar dois números")
    print("[2] - Verificar maioridade")
    print("[0] - Sair")
    opcao = int(input(""))

    if opcao == 1:
        numero_um = int(input("Digite um numero: "))
        numero_dois = int(input("Digite outro numero: "))

        soma = numero_um + numero_dois
        print(f"A soma dos números é: {soma}")

    elif opcao == 2:
        idade = int(input("Digite a sua idade: "))
        
        if idade >= 18:
            print("Maior de idade!")
        else:
            print("Menor de idade!")
        
    elif opcao == 0:
        print("Saindo do sistema...")
        break
