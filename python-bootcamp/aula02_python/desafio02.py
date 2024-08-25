# Desafio: Refatorar o projeto da aula anterior evitando Bugs!

'''
Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para 
um número de ponto flutuante e prevenção de valores negativos para salário e bônus,
você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a
tentativa de conversão para garantir que os valores sejam positivos.
'''

# Instruções

CONSTANTE_BONUS = 1000

nome_usuario = str(input("Por favor, digite seu nome: "))

if len(nome_usuario) == 0:
    print("Você não digitou nenhum caractere")
    exit()

elif nome_usuario.isspace():
    print("Você digitou apenas espaços")
    exit()

try:
    salario_usuario = float(input("Agora, insira o seu salário: ").replace(",", "."))
    
    if salario_usuario < 0:
        print("Por favor, insira um salário positivo.")
        exit()

except ValueError:
    print("Por favor, insira apenas números.")

try:
    bonus_usuario = float(input("Por fim, digite o bonus recebido: ").replace(",", "."))

    if bonus_usuario < 0:
        print("Por favor, insira um salário positivo.")
        exit()    

except ValueError:
    print("Por favor, insira apenas números.")

bonus_calculado = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

print(f"Olá {nome_usuario}, o seu valor bônus foi de {bonus_calculado}")