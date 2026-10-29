limite = int(input("Digite um número: "))

if limite == 1:
    print("Não há pares no intervalo.")
elif limite < 1:
    print("Limite inválido.")
else:
    for numero in range(2, limite + 1, 2):
        print(numero)
