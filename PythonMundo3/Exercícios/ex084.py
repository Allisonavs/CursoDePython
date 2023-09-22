# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

#NA MINHA OPINIÃO, O MELHOR CÓDIGO DO EXERCICIOS 84

# Inicialização de variáveis
contador = 0  # Contador para o número de pessoas cadastradas
peso_mais_leve = float('inf')  # Inicializando com infinito positivo para encontrar o mais leve
peso_mais_pesado = float('-inf')  # Inicializando com infinito negativo para encontrar o mais pesado
pessoa_mais_leve = list()  # Lista para armazenar a pessoa mais leve
pessoa_mais_pesada = list()  # Lista para armazenar a pessoa mais pesada

while True:
    dado = list()  # Crie uma nova lista para cada pessoa.

    # Coletando informações da pessoa
    dado.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dado.append(peso)

    # Verificando se o peso é o mais leve
    if peso == peso_mais_leve:
        pessoa_mais_leve.append(dado[0])
    elif peso < peso_mais_leve:
        peso_mais_leve = peso
        pessoa_mais_leve = [dado[0]]

    # Verificando se o peso é o mais pesado
    if peso == peso_mais_pesado:
        pessoa_mais_pesada.append(dado[0])
    elif peso > peso_mais_pesado:
        peso_mais_pesado = peso
        pessoa_mais_pesada = [dado[0]]

    contador += 1  # Incrementando o contador de pessoas cadastradas

    # Solicitando a decisão do usuário para continuar ou não
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break

print()  # Linha em branco para melhorar a apresentação
print(f'Foram cadastradas {contador} pessoas')

# Verificando se há mais de uma pessoa com o mesmo peso mais pesado
if len(pessoa_mais_pesada) > 1:
    print(f'As pessoas mais pesadas pesam {peso_mais_pesado}kg são: {", ".join(pessoa_mais_pesada)}')
else:
    print(f'A pessoa mais pesada pesa {peso_mais_pesado}kg e é: {", ".join(pessoa_mais_pesada)}')

# Verificando se há mais de uma pessoa com o mesmo peso mais leve
if len(pessoa_mais_leve) > 1:
    print(f'As pessoas mais leves pesam {peso_mais_leve}kg são: {", ".join(pessoa_mais_leve)}')
else:
    print(f'A pessoa mais leve pesa {peso_mais_leve}kg e é: {", ".join(pessoa_mais_leve)}')
