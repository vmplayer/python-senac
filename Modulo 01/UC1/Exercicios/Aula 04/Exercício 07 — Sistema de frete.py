valor_compra = float(input("Digite o valor da compra: "))
regiao = input("Digite a região: ").lower()
regiao_valida = False
frete = 0

if regiao == "sul":
    frete = 15
    regiao_valida = True
elif regiao == "sudeste":
    frete = 20
    regiao_valida = True
elif regiao == "centro-oeste":
    frete = 25
    regiao_valida = True
elif regiao == "norte" or regiao == "nordeste":
    frete = 35
    regiao_valida = True

if regiao_valida == True:
    if valor_compra >= 300:
        frete = 0

    print(f"Valor da compra: R${valor_compra:.2f}")
    print(f"Valor do frete: R${frete:.2f}")
    print(f"Total: R${(valor_compra + frete):.2f}")
else:
    print("Região inválida.")
