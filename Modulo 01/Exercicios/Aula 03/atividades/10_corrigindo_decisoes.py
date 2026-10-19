idade = int(input("Idade: ")) #
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao == "sim": # #
    print("Participação permitida.") #
else: 
    print("Participação não permitida.")
    
# CORREÇÕES:
# L1 => O INPUT recebia uma string, e não um number.
# L4 => autorizacao estava atribuindo um valor, enquanto o if não continha o ":".
# L5 => O 'print()' estava desalinhado com os padrões do Python de identação.
