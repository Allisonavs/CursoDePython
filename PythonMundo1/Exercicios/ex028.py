from time import sleep
from random import randint

# Computador pensa em um número:
pc = randint(0, 5)

# Tela do jogo
print("=-"*43)
print('Vamos jogar? Escreva um número de 0 a 5, se você pensar no mesmo que eu, você ganha!')
print("=-"*43)

# Solicita o número para o jogador
player = int(input('Em que número eu pensei? '))

# Computador começa a "processar"
print('Processando...')
sleep(2)

# Indica se ganhou ou perdeu o jogo
if player == pc:
    print('PARABÉNS, VOCÊ GANHOU!')
else:
    print('ERRADO, VOCÊ PERDEU!')
