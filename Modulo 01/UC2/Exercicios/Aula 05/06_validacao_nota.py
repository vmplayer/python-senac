nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Diga uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida.")
    else:
        print("Nota reistrada com sucesso!")

