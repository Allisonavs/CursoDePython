# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

pessoas = list()
pessoa = dict()
mulheres = list()
acima_media = list()

while True:
    # Solicita o nome da pessoa
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    
    # Solicita o sexo da pessoa, garantindo que seja 'M' ou 'F'
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opção inválida. Tente novamente.')

    # Solicita a idade da pessoa, garantindo que seja um número válido
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
            if pessoa['idade'] <= 0:
                print('Idade inválida. Tente novamente.')
            else:
                break
        except ValueError:
            print('Idade inválida. Tente novamente.')

    # Adiciona o dicionário da pessoa à lista de pessoas
    pessoas.append(pessoa.copy())
    pessoa.clear()

    # Pergunta se deseja continuar cadastrando pessoas
    if input('Quer continuar? [S/N] ').upper().strip()[0] == 'N':
        break

# Calcula a quantidade de cadastros e a média de idade
cadastros = len(pessoas)
media_idade = sum([pessoa['idade'] for pessoa in pessoas]) / cadastros

# Cria listas de mulheres e pessoas com idade acima da média
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa['nome'])

# Exibe a quantidade de cadastros
print(f'{cadastros} cadastros registrados', end='\n\n')

# Exibe a média de idade dos cadastrados
print(f'A média de idade dos cadastrados é de: {media_idade:.0f}')

# Exibe a lista de mulheres cadastradas
print('Mulheres cadastradas:')
for mulher in mulheres:
    print(mulher)

print()

# Exibe a lista de pessoas com idade acima da média
print('Pessoas com idade acima da média:')
for pessoa in acima_media:
    print(pessoa)

print()

# Exibe a lista completa de pessoas cadastradas
print(pessoas)
