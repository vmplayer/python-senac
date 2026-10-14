nome = "Atlas"
energia = 100
distancia_metros = 0
amostras_coletadas = 0
missao_andamento = True

print(f"Nome: {nome}")
print(f"Energia: {energia}")
print(f"Distância percorrida (metros): {distancia_metros}")
print(f"Amostras coletadas: {amostras_coletadas}")
print(f"Missão em andamento: {missao_andamento}")

distancia_metros += 120
energia -= 20
print(f"{nome} percorreu {distancia_metros}M e agora tem {energia}% de energia!")

amostras_coletadas += 3
energia -= 15
print(f"{nome} agora tem {amostras_coletadas} amostras e agora tem {energia}% de energia.")

energia += 10
print(f"{nome} recarregou energia e agora tem {energia}% de energia!")

distancia_metros += 80
energia -= 25
print(f"{nome} percorreu no total {distancia_metros}M e agora tem {energia}% de energia.")

amostras_coletadas += 2
energia -= 10
print(f"{nome} agora tem {amostras_coletadas} amostras e {energia}% de energia.")

missao_andamento = False
print(f"{nome} finalizou a missão!")
