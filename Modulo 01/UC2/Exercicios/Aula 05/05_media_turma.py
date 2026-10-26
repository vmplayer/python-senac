alunos_quantidade = int(input("Quantos alunos existem na turma: "))
i = 0.0
j = 0
contador = 0

if alunos_quantidade > 0:
    while contador <= (alunos_quantidade - 1):
        i = int(input("Qual a nota do aluno? "))
        j += i
        contador += 1

    media = j / alunos_quantidade
    print(f"A média é geral da turma é: {media:.2f}.")
else:
    print("A quantidade de alunos precisa ser maior que zero.")
