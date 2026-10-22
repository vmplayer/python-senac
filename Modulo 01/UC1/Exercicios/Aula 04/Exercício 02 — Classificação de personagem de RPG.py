nome = input("Nome do personagem: ")
nivel = int(input("Nível do personagem: "))
classificacao = ""

if nivel < 1:
    print("Não é permitido o nível ser menor que um.")
else:
    if nivel >= 31:
        classificacao = "Lendário"
    elif nivel >= 16:
        classificacao = "Veterano"
    elif nivel >= 6:
        classificacao = "Guerreiro"
    else:
        classificacao = "Aprendiz"

    print("\n    === NÍVEL DO PERSONAGEM ===\n")
    print(f"Nome do personagem: {nome}")
    print(f"Classificação: {classificacao} ({nivel})")
