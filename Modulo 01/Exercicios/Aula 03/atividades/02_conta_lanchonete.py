lanche_valor = float(input("Quanto pagou no rango? "))
lanche_quantidade = float(input("Comprou uns quantos? "))
lanche_total = lanche_valor * lanche_quantidade
desconto = lanche_total
desconto_aplicado = False

if lanche_total > 0:
    if lanche_total >= 50:
        desconto = lanche_total * 0.10
        desconto_aplicado = True
else:
    print("O valor deve ser maior que zero.")
lanche_novo = lanche_total - desconto

print(f"Valor total INICIAL: R${lanche_total:.2f}")
if desconto_aplicado == True:
    print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor final: R${lanche_novo:.2f}")
