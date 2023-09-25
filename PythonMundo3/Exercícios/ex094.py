# Crie um programa que leia nome, sexo e idade de várias pessoas, gurdando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres
# D) Uma lista com tododas as pessoas com idade acima da média

dados = dict()
dados_total = list()
idade_total = idade_media = 0
mulheres = list()
while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]
    dados['idade'] = int(input('Idade: '))

    idade_total += dados['idade']
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    dados_total.append(dados.copy())
    dados.clear()


    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha in 'N':
        break

print(dados_total)

idade_media = idade_total / len(dados_total)

print(f'- O grupo tem {len(dados_total)} pessoas.')
print(f'- A média de idade é {idade_media:.2f} anos.')
print('- As mulheres cadastradas foram:', end=' ')
for mulher in mulheres:
    print(mulher, end=' ')
print('- Lista das pessoas que estão acima da média: ')
