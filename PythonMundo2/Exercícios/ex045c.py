# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

#Dentro da lista o computador faz sua escolha

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#O programa mostra as opções para o jogador

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

#O programa pede que o jogador escolha a sua jogada

jogador = int(input('Qual é a sua jogada? '))

#O programa faz um suspense antes de continuar

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)


#O programa mostra as escolhas dos jogadores

print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)
print('')

#O programa indica o resultado final

if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
