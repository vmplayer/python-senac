salario = int(input("Informe o salário mensal: "))
valor_pedido = int(input("Informe o valor desejado para o empréstimo: "))
parcelas = int(input("Informe a quantidade de parcelas desejada: "))
valor_parcelas = valor_pedido / parcelas

if parcelas < 1 or parcelas > 48:
    print("Você não pode utilizar esta quantidade de parcelas. Coloque um valor entre 1 e 48.")
else:
    if salario >= 2000:
        if valor_pedido <= (salario * 10):
            if valor_parcelas <= (salario * 0.3):
                print("O seu pedido foi atendido com sucesso!")

                print(f"Salário: R${salario:.2f}")
                print(f"Valor do empréstimo: R${valor_pedido:.2f}")
                print(f"Quantidade de parcelas: {parcelas}")
                print(f"Valor por parcela: R${valor_parcelas:.2f}")
            else:
                print("O valor de cada parcela sucede 30% do seu salário. Escolha um valor menor!")
        else:
            print("O seu pedido de empréstimo é 10 vezes maior que o seu salário.")
    else:
        print("O seu salário é insuficiente para o pedido!")
