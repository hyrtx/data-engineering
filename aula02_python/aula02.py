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

# Strings

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Escreve um texto: ").upper()
print(texto)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = input("Digite o seu nome completo: ").lower()
print(nome_usuario)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, 
# imprima esta frase sem espaços em branco no início e no final.
frase = input("Escreva uma frase: ").strip()
print(frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
# em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
lista_data = data_usuario.split("/")
print(f"Dia: {lista_data[0]}; Mês: {lista_data[1]}; Ano: {lista_data[2]}.")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_usuario_1 = input("Digite uma palavra: ")
string_usuario_2 = input("Digite outra palavra: ")
resultado = string_usuario_1 + " " + string_usuario_2
print(resultado)

# Booleanos

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário 
# e retorne o resultado da operação AND entre elas.
valor_1 = (input("Digite True ou False: "))
valor_2 = (input("Novamente, digite True ou False: "))

if valor_1 == "True":
    valor_1 = True
else:
    valor_1 = False
if valor_2 == "True":
    valor_2 = True
else:
    valor_2 = False

resultado = valor_1 and valor_2
print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário
#  e retorne o resultado da operação OR.
valor_1 = (input("Digite True ou False: "))
valor_2 = (input("Novamente, digite True ou False: "))

if valor_1 == "True":
    valor_1 = True
else:
    valor_1 = False
if valor_2 == "True":
    valor_2 = True
else:
    valor_2 = False

resultado = valor_1 or valor_2
print(resultado)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.