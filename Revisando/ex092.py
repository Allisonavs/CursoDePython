# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contração e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)

from datetime import datetime

cadastro = dict()

# Solicita o nome do usuário
cadastro['nome'] = str(input('Nome: '))

# Solicita o ano de nascimento do usuário
cadastro['ano_nascimento'] = int(input('Ano de nascimento: '))

# Solicita o número da carteira de trabalho do usuário
cadastro['carteira_trabalho'] = int(input('Carteira de trabalho (0 não tem): '))

# Calcula a idade do usuário com base no ano atual
ano_atual = datetime.now().year
cadastro['idade'] = ano_atual - cadastro['ano_nascimento']

# Se a carteira de trabalho for diferente de zero, solicita mais informações
if cadastro['carteira_trabalho'] != 0:
    # Solicita o ano de contratação do usuário
    cadastro['ano_contrataçao'] = int(input('Ano de contratação: '))
    
    # Solicita o salário do usuário
    cadastro['salario'] = float(input('Salário: R$'))
    
    # Calcula o ano de aposentadoria com base no ano de contratação e 35 anos de contribuição
    cadastro['aposentadoria'] = cadastro['ano_contrataçao'] + 35 - cadastro['ano_nascimento']

# Exibe o dicionário com os dados cadastrados
print(cadastro)

# Exibe os dados cadastrados de forma mais organizada
for k, v in cadastro.items():
    print(f'{k.capitalize()} tem o valor {v}')
