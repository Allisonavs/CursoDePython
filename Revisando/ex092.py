# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contração e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)

from datetime import date

dados = dict()

dados['nome'] = input('Nome: ')

ano_de_nascimento = int(input('Ano de Nascimento: '))

dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

dados['idade'] = date.today().year - ano_de_nascimento

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))

    salario = float(input('Salário: R$'))

    dados['salário'] = f'R${salario:.2f}'

    dados['aposentadoria'] = dados['idade'] + 35

print()

print(dados)

print()

for chave, valor in dados.items():
    print(f'{chave.title()} tem o valor {valor}')
