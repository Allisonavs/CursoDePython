# Faça um programa que ajude um jogador da Mega Sena a cria palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

# Inicializa uma lista vazia para armazenar os números de cada jogo.
lista = list()
sorteios = list()

# Imprime uma linha de separação no início do programa.
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

# Solicita ao usuário a quantidade de jogos a serem sorteados.
jogos = int(input('Quantos jogos você quer que sejam sorteados? '))

# Loop para criar e imprimir os jogos.
for jogo in range(jogos):
    for sorteio in range(6):
        # Gera um número aleatório entre 1 e 60.
        num = randint(1, 60)

        # Verifica se o número já foi sorteado anteriormente.
        while num in lista:
            # Se sim, gera um novo número até que seja único.
            num = randint(1, 60)

        # Adiciona o número único à lista do jogo atual.
        if num not in lista:
            lista.append(num)

    # Ordena a lista de números do jogo.
    lista.sort()

    sorteios.append(lista[:])

    # Aguarda por um curto período de tempo (0,5 segundos).
    sleep(0.5)

    # Imprime o jogo atual com seu número de ordem.
    print(f'{jogo + 1}º Jogo: {lista}')

    # Limpa a lista para o próximo jogo.
    lista.clear()
