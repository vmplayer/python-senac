exemplares_disponiveis = 8

print(f"Exemplares disponíveis: {exemplares_disponiveis}.")
retirada = int(input("Quantos exemplares você deseja retirar? "))

if retirada <= 0:
    print("O pedido é inválido.")
elif retirada > exemplares_disponiveis:
    print("Não há exemplares o suficiente em estoque.")
else:
    exemplares_disponiveis -= retirada
    print(f"Estoque disponível: {exemplares_disponiveis}.")
    