# Crie um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Importando a função randint da biblioteca random
from random import randint

# Inicializando a variável para contar as vitórias consecutivas
vc = 0

#Tela inicial
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)

# Iniciando um loop de repetição infinito
while True:
    # Gerando um número aleatório para o computador entre 1 e 5
    computador = randint(1, 5)

    # Solicitando ao jogador que escolha um número
    jogador = int(input('Jogue seu número: '))

    # Calculando a soma do número do jogador com o número do computador
    resultado = computador + jogador

    # Solicitando ao jogador que escolha entre Par (P) ou Ímpar (I)
    escolha = input('Par ou Ímpar? [P/I] ').upper().strip()[0]

    # Exibindo os números jogados e o resultado da soma
    print('-'*60)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} ', end='')

    # Verificando se a soma é par
    if resultado % 2 == 0:
        print('DEU PAR')
        print('-'*60)
        # Verificando a escolha do jogador e determinando o resultado
        if escolha == 'P':
            print('Você VENCEU!')
            vc += 1
        elif escolha == 'I':
            print('Você PERDEU!')
            break  # Encerrando o loop se o jogador escolher ímpar

    # Caso a soma seja ímpar
    if resultado % 2 != 0:
        print('DEU ÍMPAR')
        print('-'*60)
        # Verificando a escolha do jogador e determinando o resultado
        if escolha == 'I':
            print('Você VENCEU!')
            vc += 1
        elif escolha == 'P':
            print('Você PERDEU!')
            break  # Encerrando o loop se o jogador escolher par

    # Exibindo mensagem para jogar novamente
    print('Vamos jogar novamente!')
    print('-='*30)

# Exibindo o número de vitórias consecutivas ao final do jogo
print(f'Vitórias consecutivas: {vc}')

# Mensagem de fim de jogo
print('Fim de jogo')




