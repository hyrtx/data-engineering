# Exercícios

# 1. Lista de números ao quadrado
numeros: list = list(range(1, 11))
numeros_quadrado: list = []

for n in numeros:
    numero_quadrado: int = n ** 2
    numeros_quadrado.append(numero_quadrado)

print(numeros_quadrado)

# 2. Modificar lista de linguagens
linguagens: list = ["Python", "Java", "C++", "JavaScript"]
linguagens.pop()
linguagens.append("R")
print(linguagens)

# 3. Informações de um livro
livro: dict = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}

for k, v in livro.items():
    print(f"{k}: {v}")

# 4. Contar ocorrências de caracteres
string: str = "Bootcamp de Python, preparando para a Engenharia de Dados"
string_tratada: str = string.lower().strip().replace(",", "").replace(".", "")
ocorrencias: dict = {}

for c in string_tratada:
  ocorrencias[c] = ocorrencias.get(c, 0) +1

print(ocorrencias)

# 5. Preço total da lista de compras
lista_compras: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
soma_precos: list = []

for item in lista_compras:
   soma_precos.append(precos[item])

print(f"Preço Total: {sum(soma_precos)}")
   
# 6. Eliminação de Duplicatas
'''
Dada uma lista de emails, remover todos os duplicados.
'''
emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_tratados: list = list(set(emails))

print(emails_tratados)

# 7. Filtragem de Dados
'''
Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
'''
idades: list = [22, 15, 30, 17, 18]
idades_filtradas: list = []

for idade in idades:
   if idade >= 18:
      idades_filtradas.append(idade)

print(idades_filtradas)

# 8. Ordenação Personalizada
'''
Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
'''
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas.sort(key= lambda x:x["nome"])
print(pessoas)

# 9. Agregação de Dados
'''
Dado um conjunto de números, calcular a média.
'''
numeros: list = [10, 20, 30, 40, 50]
media: float = sum(numeros) / len(numeros)
print(media)

# 10. Divisão de Dados em Grupos
'''
Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
'''
valores: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares: list = []
impares: list = []

for valor in valores:
  if valor % 2 == 0:
    pares.append(valor)
  else:
    impares.append(valor)

print(f"Valores Pares: {pares}")
print(f"Valores Ímpares: {impares}")

# 11. Atualização de Dados
'''
Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
'''
produtos: list = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
   if produto["id"] == 2:
      produto["valor"] = 90

print(produtos)

# 12. Fusão de Dicionários
'''
Dado dois dicionários, fundi-los em um único dicionário.
'''

dicionario1: dict = {"a": 1, "b": 2}
dicionario2: dict = {"c": 3, "d": 4}
dicionario_fundido: dict = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
'''
Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
'''
estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_c_qtd: dict = {}

for k, v in estoque.items():
   if v > 0:
      estoque_c_qtd[k] = v

print(estoque_c_qtd)

# 14. Extração de Chaves e Valores
'''
Dado um dicionário, criar listas separadas para suas chaves e valores.
'''

dicionario: dict = {"a": 1, "b": 2, "c": 3}
chaves: list = []
valores: list = []

for k, v in dicionario.items():
   chaves.append(k)
   valores.append(v)

print(chaves)
print(valores)

# 15. Contagem de Frequência de Itens
'''
Dada uma string, contar a frequência de cada caractere usando um dicionário.
'''

texto = "engenharia de dados"
frequencia: dict = {}

for s in texto:
   frequencia[s] = frequencia.get(s, 0) + 1

print(frequencia)
      
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

lista_numeros: list = [10, 20, 30, 40, 50]

def somar_numeros(numeros: list) -> float:
   numeros_somados: float = sum(numeros)

   return numeros_somados
  
print(somar_numeros(lista_numeros))

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e 
# False caso contrário.

def identificar_numero_primo(numero: int) -> int:
   if numero < 2:
      return False
   
   for i in range(2, numero +1):
      if numero % 1 == 0:
         if i == numero:
            return True
         else:
            return False
  
print(identificar_numero_primo(7))

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def inverter_string(texto: str) -> str:
   return texto[::-1]

print(inverter_string("Análise de Dados"))

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

lista_de_numeros: list = [10, 20, 30, 40, 50]

def pares(lista_numeros: list, numero: int) -> list:
   nova_lista_numeros: list = []
   for n in lista_numeros:
      numero_somado: int = n + numero
      nova_lista_numeros.append(numero_somado)
   
   return nova_lista_numeros

print(pares(lista_de_numeros, 100))

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

def ordenar_dicionario(dicionario: dict) -> list:
   chaves: list = []
   for k, v in dicionario.items():
      chaves.append(k)
   chaves.sort()
   return(chaves)

frutas = {
   "Banana": 10,
   "Maçã": 20,
   "Ameixa": 30,
   "Uva": 40,
   "Amora": 50,
   "Morango": 60,
   "Pêra": 70
}

print(ordenar_dicionario(frutas))


