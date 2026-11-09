pontuacoes: list[int] = []

while True:
    print("\n=== REGISTROS DO ROBÔ ===\n")
    print("[1] - Registrar pontuação")
    print("[2] - Mostrar relatório")
    print("[3] - Desfazer o último registro")
    print("[0] - Sair")
    opcao: str = input("Opção: ")

    if opcao == "1":
        reg: int = 