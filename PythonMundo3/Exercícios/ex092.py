# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contração e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)

# Importando a classe 'date' do módulo 'datetime'
from datetime import date

# Criando um dicionário vazio para armazenar informações
dados = dict()

# Solicitando e armazenando o nome do usuário
dados['nome'] = input('Nome: ')

# Solicitando e armazenando o ano de nascimento do usuário
ano_de_nascimento = int(input('Ano de Nascimento: '))

# Solicitando e armazenando o status da Carteira de Trabalho (CTPS) do usuário
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# Calculando a idade do usuário com base no ano de nascimento e o ano atual
dados['idade'] = date.today().year - ano_de_nascimento

# Verificando se o usuário possui uma CTPS
if dados['CTPS'] != 0:
    # Solicitando e armazenando o ano de contratação
    dados['contratação'] = int(input('Ano de contratação: '))

    # Solicitando e armazenando o salário do usuário como um número em ponto flutuante
    salario = float(input('Salário: R$'))

    # Formatando o valor do salário como uma string com duas casas decimais e adicionando a unidade monetária
    dados['salário'] = f'R${salario:.2f}'

    # Calculando a idade de aposentadoria estimada (idade atual + 35 anos)
    dados['aposentadoria'] = dados['idade'] + 35

# Imprimindo uma linha em branco para separar a saída
print()

# Imprimindo os dados coletados no dicionário
print(dados)

# Imprimindo uma linha em branco para separar a saída
print()

# Iterando sobre os itens do dicionário e imprimindo as informações
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')
