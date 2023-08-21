# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homem foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

# Inicializando as variáveis para contar quantidades
m18 = 0  # Contador de pessoas com mais de 18 anos
h = 0  # Contador de homens cadastrados
mm20 = 0  # Contador de mulheres com menos de 20 anos

# Iniciando um loop de repetição infinito
while True:
    #Tela inicial
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    # Capturando a idade e o sexo da pessoa
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    #Verifica se é uma resposta válida:
    while sexo not in 'MF':
        print('Opção inválida, tente novamente')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    # Verificando se a idade é maior que 18 e incrementando o contador
    if idade > 18:
        m18 += 1

    # Verificando se o sexo é masculino e incrementando o contador
    if sexo == 'M':
        h += 1

    # Verificando se o sexo é feminino e a idade é menor que 20, incrementando o contador
    if sexo == 'F' and idade < 20:
        mm20 += 1

    # Perguntando se o usuário deseja continuar ou encerrar o programa
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    # Verifica se é uma resposta válida:
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    # Encerrando o loop se a escolha for 'N'
    if escolha == 'N':
        break

# Exibindo os resultados das contagens ao final do programa
print(f'{m18} pessoas têm mais de 18 anos')
print(f'{h} homens foram cadastrados')
print(f'{mm20} mulheres têm menos de 20 anos')
