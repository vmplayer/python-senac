nota = float(input("Diga a sua nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida.")
else:
    nota_dois = float(input("Diga a sua nota: "))

    if nota_dois < 0 or nota_dois > 10:
        print("Nota inválida")
    else:
        media = (nota + nota_dois) / 2
        if media < 5:
            print(f"Nota total: {media}. \nSituação: Reprovado!")
        elif media < 7:
            print(f"Nota total: {media}. \nSituação: Recuperação")
        elif media <= 10:
            print(f"Nota total: {media}. \nSituação: Aprovado")
