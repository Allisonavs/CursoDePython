# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

#Crio a variavel do total de números que ele pode ser divisível

tot = 0

#O programa pede ao usuário um número

n = int(input('Digite um número: '))

#É criado o laço, mostrando a contagem de 1 até o número digitado

for c in range(1, n + 1):
    if n % c == 0:    # Se o número for divisível pela contagem, ele será pintado de amarelo
        print('\033[33m', end='')
        tot += 1
    else:             # Se o número não for divisível pela contagem, ele será pintado de vermelho
        print('\033[31m', end='')
    print(f'{c}', end=' ')

#O programa exibe o número de vezes que ele foi divisivel

print(f'\n\033[mO número {n} foi divisível {tot} vezes')

#O programa mostra ao usuário se ele é ou não primo

if tot == 2:          # O número só será primo se ele for divisivel por apenas 2 número, sendo 1 e ele mesmo
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
