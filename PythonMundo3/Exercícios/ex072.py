#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso


# Lista de palavras em português representando números de 0 a 20
n_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
             'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
             'onze', 'doze', 'treze', 'quatorze', 'quinze',
             'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Variável para armazenar a escolha do usuário
escolha = ''

# Loop principal, continuará executando até que seja interrompido pelo usuário
while True:

    # Loop interno para obter um número válido entre 0 e 20
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 20 >= n >= 0:
            break
        print('Tente novamente. ', end='')

    # Exibição da representação por extenso do número inserido
    print(f'Você digitou o número {n_extenso[n]}')

    # Obtendo a escolha do usuário sobre continuar ou não, e pegando a primeira letra
    escolha = input('Deseja ver mais números por extenso? [S/N] ').upper().strip()[0]

    # Loop para garantir que a escolha seja válida (S ou N)
    while escolha not in 'SN':
        print('Opção inválida, tente novamente')
        escolha = input('Deseja ver mais números por extenso? [S/N] ').upper().strip()[0]

    # Se a escolha for 'N', o programa é interrompido
    if escolha == 'N':
        break

# Exibição ao final do programa
print('Fim do Programa')
