# Exercícios de Python - If, Elif e Else

## Objetivo

Praticar estruturas condicionais (`if`, `elif` e `else`) para desenvolver o raciocínio lógico e consolidar os conceitos aprendidos até agora.

---

# Nível 1 - Básico

## 1. Verificar Maioridade

Crie um programa que solicite a idade do usuário e informe se ele é maior ou menor de idade.

### Exemplo

    Digite sua idade: 20
    Você é maior de idade.

---

## 2. Número Positivo, Negativo ou Zero

Solicite um número ao usuário e informe se ele é:

- Positivo
- Negativo
- Zero

### Exemplo

    Digite um número: -5
    Número negativo.

---

## 3. Aprovação Escolar

Peça a nota de um aluno.

### Regras

- Nota maior ou igual a 7 → Aprovado
- Nota menor que 7 → Reprovado

### Exemplo

    Digite sua nota: 8
    Aluno aprovado.

---

## 4. Número Par ou Ímpar

Solicite um número inteiro e informe se ele é:

- Par
- Ímpar

### Dica

Utilize o operador `%` (módulo).

### Exemplo

    Digite um número: 10
    Número par.

---

## 5. Verificação de Senha

Defina uma senha fixa:

    senha_correta = "python123"

Peça uma senha ao usuário e informe se ela está correta.

### Exemplo

    Digite a senha: python123
    Acesso permitido.

---

# Nível 2 - Intermediário

## 6. Comparação de Dois Números

Solicite dois números e informe:

- Qual deles é maior
- Ou se são iguais

### Exemplo

    Digite o primeiro número: 8
    Digite o segundo número: 15

    O segundo número é maior.

---

## 7. Calculadora Simples

Solicite:

- Primeiro número
- Segundo número
- Operação

### Operações Permitidas

    +
    -
    *
    /

Utilize `if`, `elif` e `else` para realizar a operação escolhida.

### Exemplo

    Digite o primeiro número: 10
    Digite o segundo número: 2
    Digite a operação: /

    Resultado: 5

---

## 8. Sistema de Desconto

Peça o valor da compra.

### Regras

- Compras acima de R$100 recebem 10% de desconto.
- Compras de até R$100 não recebem desconto.

### Exemplo

    Valor da compra: 150

    Desconto aplicado.
    Valor final: R$135,00

---

## 9. Sistema de Login

Utilize os dados:

    usuario_correto = "admin"
    senha_correta = "1234"

Solicite usuário e senha e informe:

- Login realizado
- Usuário ou senha incorretos

### Exemplo

    Usuário: admin
    Senha: 1234

    Login realizado com sucesso.

---

## 10. Ano Bissexto (Versão Simplificada)

Solicite um ano e informe se ele é divisível por 4.

### Exemplo

    Digite um ano: 2024

    Ano bissexto.

---

# Nível 3 - Desafio

## 11. Simulador de Semáforo

Peça ao usuário uma cor.

### Regras

- Verde → Pode passar
- Amarelo → Atenção
- Vermelho → Pare
- Qualquer outro valor → Cor inválida

### Exemplo

    Digite uma cor: verde

    Pode passar.

---

## 12. Classificação de Temperatura

Solicite uma temperatura.

### Regras

- Menor que 15 → Frio
- Entre 15 e 30 → Agradável
- Acima de 30 → Quente

### Exemplo

    Digite a temperatura: 33

    Quente.

---

## 13. Classificação de Triângulo

Solicite três lados.

### Regra

Se todos os lados forem iguais:

    lado1 == lado2 == lado3

Informe:

    Triângulo equilátero

Caso contrário:

    Outro tipo de triângulo

### Exemplo

    Lado 1: 5
    Lado 2: 5
    Lado 3: 5

    Triângulo equilátero.

---

## 14. Sistema de Notas Completo

Solicite a nota de um aluno.

### Regras

- Nota >= 9 → Excelente
- Nota >= 7 → Bom
- Nota >= 5 → Recuperação
- Nota < 5 → Reprovado

### Exemplo

    Digite a nota: 8

    Bom desempenho.

---

## 15. Pedra, Papel ou Tesoura

O computador possui uma escolha fixa:

    computador = "pedra"

Solicite a jogada do usuário.

Determine:

- Vitória
- Derrota
- Empate

Utilizando apenas `if`, `elif` e `else`.

### Exemplo

    Digite sua jogada: papel

    Você venceu!

---

# Mega Desafio

## Sistema de Menu Interativo

Crie um programa que apresente o seguinte menu:

    1 - Verificar idade
    2 - Par ou Ímpar
    3 - Calculadora
    4 - Sair

Utilize `if`, `elif` e `else` para executar a opção escolhida.

### Exemplo

    ===== MENU =====
    1 - Verificar idade
    2 - Par ou Ímpar
    3 - Calculadora
    4 - Sair

    Escolha uma opção: 2

O programa deverá executar a funcionalidade correspondente.

---

# Ordem Recomendada de Estudos

1. Verificar Maioridade
2. Número Positivo ou Negativo
3. Aprovação Escolar
4. Par ou Ímpar
5. Verificação de Senha
6. Comparação de Dois Números
7. Calculadora Simples
8. Sistema de Login
9. Sistema de Notas Completo
10. Pedra, Papel ou Tesoura
11. Mega Desafio

---

# Objetivo Final

Ao concluir todos os exercícios, você deverá ser capaz de:

- Utilizar `if`, `elif` e `else` com confiança;
- Trabalhar com entradas do usuário (`input`);
- Fazer comparações numéricas e textuais;
- Criar menus simples;
- Resolver problemas utilizando lógica condicional;
- Estar preparado para aprender laços de repetição (`while` e `for`).