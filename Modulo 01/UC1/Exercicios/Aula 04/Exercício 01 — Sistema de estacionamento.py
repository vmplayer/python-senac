tempo = int(input("Digite as horas nas quais o veículo ficou estacionado: "))
valor = 0

if tempo <= 0:
    print("O tempo precisa ser maior que zero.")
else:
    if tempo > 5:
        valor = 30.00
    elif tempo > 2:
        valor = 20.00
    else:
        valor = 10.00
    
    print(f"Valor a pagar: R${valor:.2f}.")
