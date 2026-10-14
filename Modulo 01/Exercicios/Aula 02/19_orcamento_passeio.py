total_alunos = 20
onibus = 600.00
ingresso_valor = 15.00
lanche_valor = 10.00

ingresso_total = ingresso_valor * total_alunos
lanches_total = lanche_valor * total_alunos
total = onibus + ingresso_total + lanches_total
aluno = total / total_alunos

print(f"Valor total dos ingressos: R$ {ingresso_total}")
print(f"Valor total dos lanches: R$ {lanches_total}")
print(f"Valor do Ônibus: R$ {onibus}")
print(f"Valor total do passeio: R$ {total}")
print(f"Valor total por aluno: R$ {aluno}")

total_alunos = 25

ingresso_total = ingresso_valor * total_alunos
lanches_total = lanche_valor * total_alunos
total = onibus + ingresso_total + lanches_total
aluno = total / total_alunos

print("\n ----- \n")

print(f"Valor total dos ingressos: R$ {ingresso_total}")
print(f"Valor total dos lanches: R$ {lanches_total}")
print(f"Valor do Ônibus: R$ {onibus}")
print(f"Valor total do passeio: R$ {total}")
print(f"Valor total por aluno: R$ {aluno}")

# Pois há mais alunos para fazer a divisão dos valores, principalmente do valor do ônibus que é único, exemplo:
# Se eu dividir 600 reais para duas pessoas, cada uma paga 300 reais, se for para 6 pessoas, cada uma paga 100 reais.
