id_msg = input("Identificação da mensagem: ")
tempo_disp = float(input("Tempo disponível: "))
tempo_nec = float(input("Tempo necessário: "))
risco = input("A mensagem indica risco imediato? (sim/nao): ").lower()
pista = input("A mensagem contém uma pista recorrente? (sim/nao): ").lower()
prioridade = ""
tempo_restante = 0.00

if tempo_disp <= 0 or tempo_nec <= 0:
    print("Tempo inválido.")
else:
    if (risco == "sim" or risco == "nao") and (pista == "sim" or pista == "nao"):
        if tempo_nec > tempo_disp:
            prioridade = "Solicitar apoio: tempo insuficiente"
        elif tempo_nec <= tempo_disp and risco == "sim":
            prioridade = "Prioridade máxima"
            tempo_restante = tempo_disp - tempo_nec
        elif tempo_nec <= tempo_disp and pista == "sim":
            prioridade = "Prioridade alta"
            tempo_restante = tempo_disp - tempo_nec
        else:
            prioridade = "Prioridade normal"
            tempo_restante = tempo_disp - tempo_nec

        print(f"Identificação da mensagem: {id_msg}")
        print(prioridade)
        print(f"Tempo restante: {tempo_restante}")
    else:
        print("Resposta inválida.")
    
# Se há risco imediato, mas falta tempo, qual resultado aparece? Justifiquem com a ordem das condições e discutam por que um programa real precisaria de regras definidas por pessoas responsáveis por esse contexto.
#
# Retorna "Tempo insuficiente", pois ele cai no if/else e a primeira condição a ser testada é o tempo.
        
# Resultado esperado

# Prioridade máxima
# Tempo insuficiente
# Prioridade alta
# Prioridade normal
# Prioridade máxima
# Tempo inválido
# Resposta inválida
# Tempo inválido
        
# 60 60 nao nao
# Prioridade normal