# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


contador = 0
peso_mais_leve = float('inf')
peso_mais_pesado = float('-inf')
pessoa_mais_leve = list()
pessoa_mais_pesada = list()

while True:
    dado = list()  # Crie uma nova lista para cada pessoa.

    dado.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dado.append(peso)

    if peso == peso_mais_leve:
        pessoa_mais_leve.append(dado[0])
    elif peso < peso_mais_leve:
        peso_mais_leve = peso
        pessoa_mais_leve = [dado[0]]

    if peso == peso_mais_pesado:
        pessoa_mais_pesada.append(dado[0])
    elif peso > peso_mais_pesado:
        peso_mais_pesado = peso
        pessoa_mais_pesada = [dado[0]]

    contador += 1

    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break

print()
print(f'Foram cadastradas {contador} pessoas')

if len(pessoa_mais_pesada) > 1:
    print(f'As pessoas mais pesadas pesam {peso_mais_pesado}kg são: {", ".join(pessoa_mais_pesada)}')
else:
    print(f'A pessoa mais pesada pesa {peso_mais_pesado}kg e é: {", ".join(pessoa_mais_pesada)}')

if len(pessoa_mais_leve) > 1:
    print(f'As pessoas mais leves pesam {peso_mais_leve}kg são: {", ".join(pessoa_mais_leve)}')
else:
    print(f'A pessoa mais leve pesa {peso_mais_leve}kg e é: {", ".join(pessoa_mais_leve)}')
