salario = int(input("Informe o salário mensal: "))
valor_pedido = int(input("Informe o valor desejado para o empréstimo: "))
parcelas = int(input("Informe a quantidade de parcelas desejada: "))

if salario >= 2000:
    if valor_pedido < (salario * 10):
        print("Continuar depois...")
    else:
        print("O seu pedido de empréstimo é 10 vezes maior que o pedido.")
else:
    print("O seu salário é insuficiente para o pedido!")