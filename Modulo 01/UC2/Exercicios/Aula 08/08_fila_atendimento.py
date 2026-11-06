fila: list[str] = []

while True:
    print('\n=== MENU ===')
    print('[1] - Adicionar pessoa no final da fila')
    print('[2] - Atender a primeira pessoa')
    print('[3] - Mostrar a fila e sua quantidade de pessoas')
    print('[0] - Sair')
    opcao: int = int(input("Opção: "))
    permitido: list[int] = [0, 1, 2, 3]
    if opcao == 1:
        add: str = input("Nome da pessoa: ")
        fila.append(add)
    elif opcao == 2:
        print(f"{fila[0]} atendido!")
        fila.pop(0)
    elif opcao == 3:
        for pessoa in fila:
            print(pessoa)
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")
