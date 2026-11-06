numeros: list[int] = []
numeros_pares: list[int] = []

for _ in range(0, 8):
    numero: int = int(input("Digite um número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"Números: {numeros}")
print(f"Números pares: {numeros_pares}")
