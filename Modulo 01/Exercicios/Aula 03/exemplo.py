import os


quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado!")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero.")
