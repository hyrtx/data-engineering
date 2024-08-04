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
   
