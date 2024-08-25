# Desafio: Cálculo de Bônus com Entrada do Usuário

'''
Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário 
mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando 
o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
'''

# Instruções

CONSTANTE_BONUS = 1000
# 01. O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = str(input("Por favor, digite seu nome: "))

# 02. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Agora, insira o seu salário: "))

# 03. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode 
# ser um número decimal.
bonus_usuario = float(input("Por fim, digite o bonus recebido: "))

# 04. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus_calculado = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

# 05. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
# "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_usuario}, o seu valor bônus foi de {bonus_calculado}")





