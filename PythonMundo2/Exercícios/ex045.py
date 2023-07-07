# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

#O jogador escolhe entre pedra, papel, ou tesoura

print('Escolha:')
print('1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura')
e = input()

#O jogo fica em suspense até mostrar o resultado

sleep(1)

#O computador aleatoriza a sua escolha

ep = (randint(1,3))

#O computador indica quem ganhou

if e == '1':
    if ep == 1:
        print('(PLAYER) Pedra x Pedra (CPU)')
        print('EMPATE')
    elif ep == 2:
        print('(PLAYER) Pedra x Papel (CPU)')
        print('CPU Venceu!')
    elif ep == 3:
        print('(PLAYER) Pedra x Tesoura (CPU)')
        print('PLAYER Venceu!')

elif e == '2':
    if ep == 1:
        print('(PLAYER) Papel x Pedra (CPU)')
        print('PLAYER Venceu!')
    elif ep == 2:
        print('(PLAYER) Papel x Papel (CPU)')
        print('EMPATE')
    elif ep == 3:
        print('(PLAYER) Papel x Tesoura (CPU)')
        print('CPU Venceu!')

elif e == '3':
    if ep == 1:
        print('(PLAYER) Tesoura x Pedra (CPU)')
        print('CPU Venceu!')
    elif ep == 2:
        print('(PLAYER) Tesoura x Papel (CPU)')
        print('PLAYER Venceu!')
    elif ep == 3:
        print('(PLAYER) Tesoura x Tesoura (CPU)')
        print('EMPATE')
