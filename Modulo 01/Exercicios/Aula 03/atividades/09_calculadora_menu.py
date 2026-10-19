num_um = float(input("Digite um número: "))
num_dois = float(input("Digite outro número: "))

opcao = input("\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n\nEscolha uma opção: ")

if opcao == "1":
    resultado = num_um + num_dois
    print(f"Resultado da operação: {resultado}.")
elif opcao == "2":
    resultado = num_um - num_dois
    print(f"Resultado da operação: {resultado}.")
elif opcao == "3":
    resultado = num_um * num_dois
    print(f"Resultado da operação: {resultado}.")
elif opcao == "4":
    if num_dois == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = num_um / num_dois
        print(f"Resultado da operação: {resultado}.")
else:
    print("Opção inválida.")
