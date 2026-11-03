palavra = input("Digite uma palavra: ")
letra = input("Letra para a contagem: ")
rep = 0

for letr in palavra:
    if letr == letra:
        rep += 1

print(f"Letra {letr} repetiu {rep} vezes.")
