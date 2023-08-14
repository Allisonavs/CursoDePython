# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar [2] multiplicar [3] maior [4] novos números [5] sair do programa

escolha = ''

while escolha != '5':
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite um valor: '))

    print('\nVocê deseja: ')
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[5] Sair do programa''')

    escolha = input('\nEscolha: ')
    if escolha == '1':
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} = {soma}')

    elif escolha == '2':
        multi = v1 * v2
        print(f'A multiplicação entre {v1} * {v2} = {multi}')

    elif escolha == '3':
        if v1 > v2:
            print(f'{v1} é maior que {v2}')
        elif v2 > v1:
            print(f'{v2} é maior que {v1}')
        else:
            print(f'{v1} e {v2} são iguais')

