a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b and b != c and c != a:
            print("O triângulo é isósceles!")
        elif a == b and b == c and c == a:
            print("O triângulo é equilátero!")
        elif a != b and b != c and c != a:
            print("O triângulo é escaleno!")
    else:
        print("Triângulo inválido.")
else:
    print("Um ou mais dos números é igual ou menor que zero.")
