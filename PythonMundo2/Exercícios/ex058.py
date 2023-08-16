# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer

from time import sleep
from random import randint


# Computador pensa em um número:
pc = randint(0, 10)

# Tela do jogo
print("=-"*43)
print('Vamos jogar? Escreva um número de 0 a 10, se você pensar no mesmo que eu, você ganha!')
print("=-"*43)

# Solicita o número para o jogador
player = int(input('Em que número eu pensei? '))

# Computador começa a "processar"
sleep(0.5)

# Contador de vezes que o jogador palpitou
palpite = 0

# Enquanto o player não acertar, ele poderá continuar tentando
while player != pc:
    print('Processando...')
    sleep(0.5)

    print(f'Você errou')
    if player > pc:
        print('Menos')
    elif player < pc:
        print('Mais')
    player = int(input('Tente novamente: '))

    palpite += 1


# Indica se ganhou o jogo e quantos palpites ele precisou
if player == pc:
    print('Processando...')
    sleep(0.5)

    palpite += 1

    print('PARABÉNS, VOCÊ GANHOU!')
    print(f'Você precisou de {palpite} tentativas')
