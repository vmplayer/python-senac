nome = input("Digite o seu nome: ")

print(f"Olá, {nome}! Seja bem-vindo(a)!")

idade_txt = input("Digite a sua idade: ")

print(idade_txt)
print(type(idade_txt))

# Primeira forma de conversão
idade = int(idade_txt)

print(f"Tipo da variável 'idade_txt: {type(idade_txt)}.")
print(f"Tipo de variável 'idade' {type(idade)}.\n")
print(f"No próximo aniversário, você terá {idade + 1} anos!")

print (idade >= 18)

teste = "sim"

print(teste)
print()
print(teste.lower()) # deixa todas as letras minúsculas
print(teste.upper()) # deixa todas as letras maiúsculas
print(teste.capitalize()) # deixa apenas a primeira letra maiúscula
print("TEstE INveRtER".swapcase()) # inverte maiúsculas e minúsculas
print("helloß".casefold()) # Traduz para a fonética Unicode

teste2 = "olá, pessoal. ".capitalize() + "tudo bem?".capitalize()
print(teste2)


idade_convertida = int(input("Digite a sua idade: "))
if idade_convertida >= 18:
    print("Você atingiu a maioridade.")
elif idade_convertida < 18:
    print("Você é menor de idade.")

print("Consulta encerrada!")
