temperatura = int(input("Qual a sua temperatura? "))

if temperatura < 18:
    print("Ambiente frio.")
elif temperatura < 26:
    print("Ambiente agradável.")
else:
    print("Ambiente quente.")
