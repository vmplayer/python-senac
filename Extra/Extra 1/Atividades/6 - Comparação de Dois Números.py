num_um = int(input("Número 1: "))
num_dois = int(input("Número 2: "))

if num_um < num_dois:
    print(f"{num_dois} é maior que {num_um}.")
elif num_um > num_dois:
    print(f"{num_um} é maior que {num_dois}.")
else:
    print("Os números são iguais.")
