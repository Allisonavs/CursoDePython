# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

#É criada as variaveis do maior peso e do menor peso
maior = 0
menor = 0

#O laço é criado para perguntar o pesdo de 5 pessoas
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:    # Se for o primeiro laço, o número digitado será considerado o maior e o menor peso
        maior = peso
        menor = peso
    else:         # Se não for o primeiro laço, fara a comparação, mudando o maior e o menor, dependendo do valor digitado
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

#O programa mostra ao usuário qual o maior e qual o menor peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
