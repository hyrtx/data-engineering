from math import pi

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

# Float
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input("Escolha um número decimal: "))
numero_2 = float(input("Escolha outro número decimal: "))
resultado = numero_1 + numero_2
print(f"A soma de {numero_1} com {numero_2} é {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Escolha um número decimal: "))
numero_2 = float(input("Escolha outro número decimal: "))
resultado = (numero_1 + numero_2) / 2
print(f"A média de {numero_1} e {numero_2} é {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número
# (base e expoente fornecidos pelo usuário).
base_usuario = float(input("Escolha a base para o cálculo de potência: "))
expoente_usuario = float(input("Agora, digite o expoente: "))
resultado = base_usuario ** expoente_usuario
print(f"{base_usuario} elevado a {expoente_usuario} é {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temp_celsius = float(input("Digite a temperatura em Celsius: "))
resultado = temp_celsius * 1.8 + 32
print(f"{temp_celsius}ºC equivale a {resultado}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
from math import pi
raio = float(input("Digite o raio: "))
resultado = pi * raio ** 2
print(f"A área do circulo para um raio de {raio} é {resultado}")