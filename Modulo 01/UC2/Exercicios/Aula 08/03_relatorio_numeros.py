numeros = []
soma = 0
i = 1

for numero in range(0, 6):
    numero = int(input(f"Digite um número {i}: "))
    numeros.append(numero)

    soma += numero
    i += 1

print()
i = 1

for numero in numeros:
    i += 1
    print(f"Número {i}: {numero}")

print(f"Soma: {soma}")
print(f"Média: {soma / len(numeros)}")
print(f"Número maior: {max(numeros)}")
print(f"Número menor: {min(numeros)}")
