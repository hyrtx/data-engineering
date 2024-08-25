# Exercícios if

# Exercício 1: Verificação de Qualidade de Dados
'''
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros 
tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e 
imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
'''

quantidade = int(input("Insira a quantidade: "))
preco = float(input("Insira o preço: "))

if quantidade >= 0 and preco >= 0:
    print("Dados Válidos")
else:
    print("Dados Inválidos")

# Exercício 2: Classificação de Dados de Sensor
'''
Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'
'''

temperatura = float(input("Insira a temperatura: "))

if temperatura > 26:
    print("Alta")
elif temperatura > 18:
    print("Normal")
else:
    print("Baixa")

# Exercício 3: Filtragem de Logs por Severidade
'''
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
Dado um registro de log em formato de dicionário como 
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
'''

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log["level"] == "ERROR":
    print(log["message"])

# Exercício 4: Validação de Dados de Entrada
'''
Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir 
que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico 
encontrado.
'''

idade = int(input("Digite a idade: "))
email = input("Digite o e-mail: ")

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email:
    print("O email digitado não é válido")
else:
    print("Dados válidos")

# Exercício 5: Detecção de Anomalias em Dados de Transações
'''
Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário 
comercial (antes das 9h ou depois das 18h). 
Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.
'''

transacao = {'valor': 12000, 'hora': 20}

if transacao["valor"] > 10000 or not 9 <= transacao["hora"] <= 18:
    print("Transação suspeita")

# Exercícios for

# Exercício 6: Contagem de Palavras em Textos
'''
Dado um texto, contar quantas vezes cada palavra única aparece nele.
'''
texto = "a raposa marrom salta sobre o cachorro marrom preguiçoso"
texto_tratado = texto.replace(",", "").replace(".", "")
palavras = texto_tratado.split(" ")
quantidade_palavras = {}

for s in palavras:
    if s in quantidade_palavras:
        quantidade_palavras[s] += 1
    else:
        quantidade_palavras[s] = 1

print(quantidade_palavras)

# Exercício 7: Normalização de Dados
'''
Normalizar uma lista de números para que fiquem na escala de 0 a 1.
'''

numeros = [10, 20, 30, 40, 50]
normalizados = []

for x in numeros:
    normalizados.append((x - min(numeros)) / (max(numeros) - min(numeros)))

print(normalizados)

# Exercício 8: Filtragem de Dados Faltantes
'''
Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um 
campo específico faltando.
'''

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_invalidos = []

for usuario in usuarios:
    if usuario["email"] == "":
      usuarios_invalidos.append(usuario["nome"])

print(usuarios_invalidos)

# Exercício 9: Extração de Subconjuntos de Dados
'''
Dada uma lista de números, extrair apenas aqueles que são pares.
'''
numeros = range(1, 11)
numeros_pares = []

for n in numeros:
    if n % 2 == 0:
        numeros_pares.append(n)

print(numeros_pares)

# Exercício 10: Agregação de Dados por Categoria
'''
Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
'''
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_por_categorias = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]

    if categoria in vendas_por_categorias:
        vendas_por_categorias[categoria] += valor
    else:
        vendas_por_categorias[categoria] = valor

print(vendas_por_categorias)

# 11. Leitura de Dados até Flag
'''
Ler dados de entrada ate que uma palavra-chave específica ("sair") seja fornecida.
'''
palavras = []

while "sair" not in palavras:
    palavra = input("Escolha uma palavra: ").lower()
    palavras.append(palavra)

# 12. Validação de Entrada
'''
Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
'''
numero_escolhido = int(input("Escolha um número: "))

while not 0 <= numero_escolhido <= 10:
    numero_escolhido = int(input("Escolha um número: "))

# 13. Consumo de API Simulado
'''
Simular o consumo de uma API paginada, onde cada "página" de dados é processada em 
loop até que não haja mais páginas.
'''
pagina_atual = 1
paginas_totais = 5

while pagina_atual <= paginas_totais:
    print(f"Processamento da página {pagina_atual} feito.")
    pagina_atual += 1

print(pagina_atual)
print(paginas_totais)
print("Todas as páginas foram processadas")

# 14. Tentativas de Conexão
'''
Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
'''

tentativa = 1
tentativas_totais = 5

while tentativa <= (tentativas_totais):
    print(f"Tentativa de reconexão {tentativa} de {tentativas_totais}")
    tentativa += 1
    print("Reconectando...")

print("Não foi possível conectar")

# 15. Processamento de Dados com Condição de Parada
'''
Processar itens de uma lista até encontrar um valor específico que indica a parada.
'''

itens = [1, 2, 3, "parar", 4, 5]
i = 0

while i < len(itens):
    
    if itens[i] == "parar":
        print(f"Palavra {itens[i]} encontrada. Encerrando o processo")
        break
    print(f"processando item {itens[i]}")
    i += 1

