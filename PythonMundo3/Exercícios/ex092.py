# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contração e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)

from datetime import date

# Cria um dicionário vazio para armazenar informações do usuário
dados = dict()

# Solicita e armazena o nome do usuário
dados['nome'] = input('Nome: ')

# Solicita e armazena o ano de nascimento do usuário
ano_de_nascimento = int(input('Ano de Nascimento: '))

# Calcula a idade do usuário com base no ano de nascimento e o ano atual
dados['idade'] = 2018 - ano_de_nascimento

# Solicita e armazena o status da Carteira de Trabalho (CTPS) do usuário
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# Verifica se o usuário possui uma CTPS
if dados['CTPS'] != 0:
    # Solicita e armazena o ano de contratação do usuário
    dados['contratação'] = int(input('Ano de contratação: '))

    # Solicita e armazena o salário do usuário
    salario = float(input('Salário: R$'))
    # Formata o salário como uma string com duas casas decimais e adiciona a unidade monetária
    dados['salário'] = f'R${salario:.2f}'

    # Calcula o ano de aposentadoria com base no ano de contratação e adiciona 35 anos
    ano_aposentadoria = dados['contratação'] + 35
    # Calcula a idade de aposentadoria com base no ano de aposentadoria e o ano de nascimento
    idade_aposentadoria = ano_aposentadoria - ano_de_nascimento

    # Verifica se o usuário já pode se aposentar
    if idade_aposentadoria >= 65 or (idade_aposentadoria >= 62 and dados['idade'] >= 60):
        dados['aposentadoria'] = "Já pode se aposentar."
    else:
        # Calcula quantos anos faltam para a aposentadoria
        anos_para_aposentar = ano_aposentadoria - 2018
        dados['aposentadoria'] = f'Poderá se aposentar em {ano_aposentadoria} com {idade_aposentadoria} anos'

# Imprime uma linha em branco para separar a saída
print()

# Imprime os dados pessoais do usuário
print("Dados Pessoais:")
for chave, valor in dados.items():
    if chave == 'CTPS':
        print(f' - Carteira de Trabalho: {valor}')
    else:
        print(f' - {chave.title()}: {valor}')
