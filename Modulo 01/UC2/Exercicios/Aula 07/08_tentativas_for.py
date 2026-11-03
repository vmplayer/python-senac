codigo = "ROBO123"
sucesso = False

for tentativa in range(0, 3):
    print(f"=== TENTATIVA {tentativa + 1} ===")
    tenta = input("Digite o código: ")

    if tenta == codigo:
        print("Código descoberto com sucesso!")
        sucesso = True
        break

if sucesso == False:
    print("\nAs suas fichas acabaram.")
