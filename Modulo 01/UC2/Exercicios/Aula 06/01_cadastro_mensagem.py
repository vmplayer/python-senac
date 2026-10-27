nome_analista = input("Nome do analista: ")
id_msg = input("ID da mensagem: ")
quantidade_sygroup = int(input("Quantidade de grupos de símbolos: "))
tempo_analise = float(input("Tempo de análise estimado: ")) 
tempo_total = 0.00 

if quantidade_sygroup <= 0 or tempo_analise <= 0:
    print("Dados inválidos")
else:
    tempo_total = quantidade_sygroup * tempo_analise

    print()
    print("        === FICHA ===")
    print(f"Nome do analista: {nome_analista}")
    print(f"Identificação: {id_msg}")
    print(f"Quantidade de grupos: {quantidade_sygroup}")
    print(f"Tempo total: {tempo_total:.2f}")

    if tempo_total <= 60:
        print("Análise dentro do prazo.")
    else:
        print("Reorganizar o trabalho.")
    
# Por que a identificação é texto mesmo quando contém algarismos?
# Porque ela é uma string.

# Por que é adequado usar float() para o tempo por grupo?
# Porque recebe a representação dos segundos.

# True = Dentro do Prazo
# False = Reorganizar o trabalho

# Resultado Esperado - Saída obtida
# 50 - True
# 60 - True
# 65 - False
# 0 - Dados Inválidos
# -10 - Dados Inválidos
        
# 20 grupos e 2.50 minutos por grupo
# 40.5 - True 
# Aqui há número com casa decimal nos min/g
