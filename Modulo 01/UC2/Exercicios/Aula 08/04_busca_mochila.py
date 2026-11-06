mochila = ["corda", "água", "mapa", "água"]

obj = input("Qual item deve ser procurado na mochila? ").lower()
occ = 0

for item in mochila:
    if item == obj:
        occ += 1

if occ > 0:
    print(f"Ocorrências: {occ}")
else:
    print("O item não foi achado.")
