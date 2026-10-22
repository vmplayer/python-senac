nome = input("Digite o nome do personagem: ")
hp = int(input("Vida total do personagem: "))
atk = int(input("Quantidade de pontos de ataque: "))
hp_inimigo = int(input("Digite a quantidade total de vida do inimigo: "))
def_inimigo = int(input("Quantidade de pontos de defesa do inimigo: "))

dano = atk - def_inimigo

if hp <= 0:
    print("Você não pode atacar.")
else:
    if dano <= 0:
        print("Você não causou dano.")
    else:
        hp_inimigo - dano
        print(f"Dano causado: {dano}")
        if hp_inimigo <= 0:
            hp_inimigo = 0
            print("O inimigo foi derrotado!")
        else:
            print("O inimigo sobreviveu!")
            print(f"\nVida do inimigo: {hp_inimigo}")
