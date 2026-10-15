# media = float(input("Digite a média de 0 a 10: "))

# if media >= 7:
#     print("Aprovado.")
# elif media >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

# temperatura = float(input("Temperatura: "))

# if temperatura >= 100:
#     print("Calor intenso.")
# elif temperatura >= 30 and temperatura <= 50:
#     print("Dia quente.")

# idade = int(input("Idade: "))
# vagas = int(input("Vagas disponíveis: "))

# if idade >= 14 and vagas > 0:
#     print("Inscrições permitidas")
# else:
#     print("fim")

# tem_ingresso = True
# idade = 16

# if idade >= 18 or tem_ingresso:
#     print("Pode entrar na festa!")

idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")

resposta = input("O robô está em manutenção? (Sim/Não): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")
    
