# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

#O programa pede que o usuário digite os dois números

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))

#O programa agora analisa qual valor é o maior e mostra para o usuário

if n1 > n2:
    print(f'O {n1} é maior')
elif n2 > n1:
    print(f'O {n2} é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
