# Desafio: Refatorar o desafio da aula 03 usando Dicionário, Type Hint e Funcões.

# Variáveis para controle do loop

CONSTANTE_BONUS: float = 1000
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

# Verificação do nome
def validacao_nome(nome_usuario: str) -> bool:
    '''
    Função para verificar se o nome digitado pelo usuário é valido, retornando False caso
    algum erro seja identificado em True caso não exista erros no nome digitado.
    '''

    # Verifica se algo foi digitado no nome, retornando False no caso de hipótese validada.
    if len(nome_usuario) == 0:
        return False
    
    # Verifica se foi digitado apenas espaços, retornando False no caso de hipótese validada.
    elif nome_usuario.isspace():
        return False
    
    # Se nenhum erro for identificado, retorna True
    else:
        return True

def salario_valido(salario_usuario: float) -> bool:
    return None

def bonus_valido(bonus_usuario: float) -> bool:
    return None


while not nome_valido:
    nome_usuario: str = input("Por favor, digite seu nome: ").strip()

    if len(nome_usuario) == 0:
        print("Você não digitou nenhum caractere")

    elif nome_usuario.isspace():
        print("Você digitou apenas espaços")
    
    else:
        nome_valido = True

# Verificação do salário
while not salario_valido:
    try:
        salario_usuario: float = float(input("Agora, insira o seu salário: ").replace(",", "."))

        if salario_usuario < 0:
            print("Por favor, insira um salário positivo.")
        
        else:
            salario_valido = True

    except ValueError:
        print("Por favor, insira apenas números.")

# Verificação do bonus
while not bonus_valido:
    try:
        bonus_usuario: float = float(input("Por fim, digite o bonus recebido: ").replace(",", "."))

        if bonus_usuario < 0:
            print("Por favor, insira um salário positivo.")
        
        else:
            bonus_valido = True

    except ValueError:
        print("Por favor, insira apenas números.")

# Cálculo do bonus
bonus_calculado: float = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

# Impressão da mensagem para o usuário
print(f"Olá {nome_usuario}, o seu valor bônus foi de {bonus_calculado}")