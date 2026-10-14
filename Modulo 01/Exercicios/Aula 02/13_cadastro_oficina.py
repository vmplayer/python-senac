nome_oficina = "Robótica para Iniciantes"
sala = "Laboratório 2"
vagas = 24
duracao_horas = 2.5
inscricoes = True

print(f"Nome da oficina: {nome_oficina}")
print(f"Sala: {sala}")
print(f"Vagas: {vagas}")
print(f"Duração do curso (em horas): {duracao_horas}")
print(f"Inscrições: {inscricoes}")

print(type(nome_oficina)) # String pois é um TEXTO informando o nome do curso.
print(type(sala)) # String pois é um TEXTO (Laboratório x).
print(type(vagas)) # INT pois é o NÚMERO de vagas.
print(type(duracao_horas)) # Float pois é o tempo em Horas.Minutos da duração total.
print(type(inscricoes)) # Bool pois é True (Inscrições Abertas) e False (Inscrições Fechadas).

