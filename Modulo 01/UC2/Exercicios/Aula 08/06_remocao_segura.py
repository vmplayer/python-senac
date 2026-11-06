nomes: list[str] = ["Ana", "Bruno", "Ana", "Carla"]

print(nomes[0:])
nome_remover: str = input("Digite o nome a ser removido: ").capitalize()

for nome in nomes:
    if nome == nome_remover:
        nomes.remove(nome)
        break
        
print(nomes[0:])

