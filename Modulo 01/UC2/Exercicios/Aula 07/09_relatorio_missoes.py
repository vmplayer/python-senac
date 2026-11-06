energia = 100
custo = 25
missoes = 0
resultado = ""
pontuacao = 0

for missao in range(0, 5):
    if energia >= custo:
        print("Missão:", missao + 1)

        while True:
            pontos = int(input("Pontuação: "))
            if pontos >= 0 and pontos <= 100:
                break

        energia -= custo
        pontuacao += pontos
        missoes += 1
    else:
        print("Energia insuficiente.")
        break

if missoes > 0:
    print(f"=== RESULTADOS ===")
    print(f"Missões realizadas: {missoes}")
    print(f"Média de pontos: {pontuacao / missoes}")
    print(f"Energia restante: {energia}")
    # Apenas será dividido por zero se estiver fora do aninhamento do if.
