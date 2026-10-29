numero = int(input("Diga um número: "))

if numero > 0:
    for num in range(1, numero + 1):
        print(num)
else:
    print("O número é igual ou menor a zero.")
