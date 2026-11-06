alunos_qtd: int = int(input("Quantidade de alunos: "))
notas: list[str] = []
soma: int = 0

if alunos_qtd > 0:
    for _ in range(0, alunos_qtd):
        while True:
            nota: int = int(input("Nota do aluno: "))
            if nota >= 0 and nota <= 10:            
                notas.append(nota)
                soma = nota
                break
            else:
                print("Nota inválida. Digite novamente.")
    print(f"Notas: {notas}")
    print(f"Média: {soma / alunos_qtd:.2f}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
else:
    print("Quantidade inválida.")
