# Exercícios de TypeError

# Exercício 21: Conversor de Temperatura

'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
'''
try:
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    print(f"{temp_celsius}ºC equivale a {temp_fahrenheit}ºF")
except ValueError:
    print("O valor digitado não é um número válido.")

# Exercício 22: Verificador de Palíndromo

'''
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para 
frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma 
string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''

try:
    frase = input("Digite uma palavra ou frase: ").lower()
    frase_limpa = "".join(char for char in frase if char.isalnum())
    frase_reversa = frase_limpa [::-1]
    valid_palindromo = (frase_limpa == frase_reversa)

    print(f"A frase {frase_limpa} ao contrário é {frase_reversa}")

    if valid_palindromo:
        print(f"A frase é um palíndromo")
    else:
        print(f"A frase não é um palíndromo")
except Exception as e:
    print(e)

# Exercício 23: Calculadora Simples

'''
Desenvolva uma calculadora simples que aceite duas entradas numéricas e 
um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e 
entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada
no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.'''

lista_operadores = ["+", "-", "*", "/"]

try:
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite outro número: "))
    operador = input("Digite um operador (+, -, *, /): ").strip()
    resultado = 0

    if operador in lista_operadores:
        if operador == "+":
            resultado = numero_1 + numero_2
        
        elif operador == "-":
            resultado = numero_1 - numero_2
        
        elif operador == "*":
            resultado = numero_1 * numero_2
        
        elif operador == "/":
            try:
                resultado = numero_1 / numero_2
            except ZeroDivisionError:
                print("Não é possível dividir por 0")

        print(f"O resultado de {numero_1} {operador} {numero_2} é: {resultado}")
        
    else:
        print("O operador não foi devidamente selecionado")

except ValueError:
    print("Erro: Entrada invalida. Se certifique de escolher números")

except Exception as e:
    print(e)
    print(type(e))

# Exercício 24: Classificador de Números

'''
Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para
assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como
"positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
'''
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# Exercício 25: Conversão de Tipo com Validação

'''
Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve
converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a
conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão 
for bem-sucedida para todos os elementos, imprima a lista de inteiros.
'''

numeros = input("Escreva uma lista de números separados por vírgula: ").replace(" ", "")
lista_numeros_str = numeros.split(",")
lista_numeros_int = []

try:
    for _ in lista_numeros_str:
        lista_numeros_int.append(int(_))
    
    print(f"Lista de Números Inteiros: {lista_numeros_int}")

except ValueError:
    print("Erro: Entrada Invalida. Por favor, digite apenas números inteiros.")