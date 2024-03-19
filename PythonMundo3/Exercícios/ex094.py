# Crie um programa que leia nome, sexo e idade de várias pessoas, gurdando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres
# D) Uma lista com tododas as pessoas com idade acima da média

# Cria um dicionário vazio para armazenar os dados de cada pessoa
dados = dict()

# Cria uma lista vazia para armazenar todos os dicionários de dados de pessoas
dados_total = list()

# Inicializa variáveis para calcular a idade média
idade_total = idade_media = 0

# Cria uma lista vazia para armazenar os nomes das mulheres
mulheres = list()

# Loop infinito para continuar a coletar dados até que o usuário decida parar
while True:
    # Solicita e armazena o nome da pessoa
    dados['nome'] = input('Nome: ')

    # Solicita e armazena o sexo da pessoa, converte para maiúsculo e pega o primeiro caractere
    dados['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]

    # Solicita e armazena a idade da pessoa
    dados['idade'] = int(input('Idade: '))

    # Adiciona a idade da pessoa à idade total para calcular a média posteriormente
    idade_total += dados['idade']

    # Verifica se a pessoa é do sexo feminino e adiciona o nome à lista de mulheres
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    # Adiciona uma cópia do dicionário de dados da pessoa à lista de dados total
    dados_total.append(dados.copy())

    # Limpa o dicionário de dados para a próxima iteração
    dados.clear()

    # Pergunta ao usuário se deseja continuar e encerra o loop se a resposta for 'N'
    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha in 'N':
        break

# Imprime todos os dados coletados
print(dados_total)

# Calcula a média de idade do grupo
idade_media = idade_total / len(dados_total)

# Imprime o número total de pessoas e a média de idade do grupo
print(f'- O grupo tem {len(dados_total)} pessoas.')
print(f'- A média de idade é {idade_media:.2f} anos.')

# Imprime os nomes das mulheres cadastradas
print('- As mulheres cadastradas foram:', end=' ')
for mulher in mulheres:
    print(mulher, end=' ')

# Imprime uma mensagem indicando que a lista das pessoas acima da média será exibida em seguida
print('- Lista das pessoas que estão acima da média: ')

