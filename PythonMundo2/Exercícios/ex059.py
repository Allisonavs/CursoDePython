# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar [2] multiplicar [3] maior [4] novos números [5] sair do programa

from time import sleep

# É definida a variável de escolha
escolha = ''

# O programa pede para o usuário digitar dois valores
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))

# É criado o laço de repetição
while escolha != '5':  # O loop continua enquanto a escolha não for '5' (Sair)

    # É apresentado o menu com as opções
    print('\nVocê deseja: ')
    print('''\033[34m
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos valores
[5] Sair do programa\033[m''')

    escolha = input('\n>>>> ')  # Solicita a escolha do usuário

    if escolha == '1':
        soma = v1 + v2
        print(f'\033[32mA soma entre {v1} + {v2} = {soma}\033[m')  # Exibe o resultado da soma

    elif escolha == '2':
        multi = v1 * v2
        print(f'\033[32mA multiplicação entre {v1} * {v2} = {multi}\033[m')  # Exibe o resultado da multiplicação

    elif escolha == '3':
        if v1 > v2:
            print(f'\033[32m{v1} é maior que {v2}\033[m')
        elif v2 > v1:
            print(f'\033[32m{v2} é maior que {v1}\033[m')
        else:
            print(f'\033[32m{v1} e {v2} são iguais\033[m')  # Exibe o resultado da comparação entre os valores

    elif escolha == '4':
        v1 = int(input('Digite um valor: '))  # Solicita novo valor para v1
        v2 = int(input('Digite um valor: '))  # Solicita novo valor para v2

    elif escolha not in '12345':
        print('\033[31mOpção inválida. Tente Novamente\033[m')
    print('='*10)
    sleep(2)
print('Fim do programa')