# Exercícios

# Inteiros
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário
numero_1 = int(input("Escolha um número inteiro: "))
numero_2 = int(input("Escolha outro número inteiro: "))
resultado = numero_1 + numero_2
print(f"A soma de {numero_1} com {numero_2} é {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
NUMERO_DIVISOR = 5
numero_usuario = int(input("Digite um número: "))
resultado = numero_usuario % 5
print(f"O resto da divisão de {numero_usuario} por {NUMERO_DIVISOR} é {resultado}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input("Escolha um número: "))
numero_2 = int(input("Escolha outro número: "))
resultado = numero_1 * numero_2
print(f"O resultado da multiplicação de {numero_1} e {numero_2} é {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_1 = int(input("Escolha um número inteiro: "))
numero_2 = int(input("Escolha outro número inteiro: "))
resultado = numero_1 // numero_2
print(f"A divisão inteira entre {numero_1} e {numero_2} é {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_usuario = int(input("Escolha um número: "))
resultado = numero_usuario ** 2
print(f"O quadrado de {numero_usuario} é{resultado}")