soma = 0
maior = 0

for numero in range(0, 6):
    numero = int(input("Digite um número: "))
    soma += numero

    if numero > 0:
        maior += 1

print('=== RESULTADOS ===')
print(f'\nSoma total dos itens: {soma}.')
print(f'Números maiores que zero: {maior}.')
