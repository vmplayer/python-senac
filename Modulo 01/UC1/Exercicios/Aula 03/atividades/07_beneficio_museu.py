idade = int(input("Digite a sua idade: "))

if idade < 0 or idade > 112:
    print("Idade inválida.")
else:
    valor_entrada = 20

    if idade < 12 or idade >= 60:
        valor_entrada = 0

    print(f"Valor da entrada: R${valor_entrada:.2f}.")
    