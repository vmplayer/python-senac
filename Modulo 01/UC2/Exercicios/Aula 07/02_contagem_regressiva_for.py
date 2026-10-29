numero = int(input("Digite um número: "))

if numero >= 0:
    for numero in range(numero, 0, -1):
        print(numero, end=" ")
    print("Lançamento realizado!")
else:
    print("Valor inválido.")
