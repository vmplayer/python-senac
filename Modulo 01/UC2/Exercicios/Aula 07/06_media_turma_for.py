alunos = int(input("Quantidade de alunos: "))
soma = 0
maior = 0
media = 0

if alunos > 0:
    for aluno in range (0, alunos):
        nota = int(input(f"Nota do aluno {aluno + 1}: "))

        while nota < 0 or nota > 10:
            nota = int(input(f"Nota do aluno {aluno + 1}: "))

        soma += nota

        if nota >= 7:
            maior += 1

    media = soma / alunos

    print("=== RESULTADOS ===")
    print(f"Média da turma: {media}")
    print(f"Notas >= 7: {maior}") 
else:
    print("Quantidade de alunos inválida.")
