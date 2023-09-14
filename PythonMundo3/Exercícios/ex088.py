# Faça um programa que ajude um jogador da Mega Sena a cria palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

qtd_jogos = int(input('Quantos jogos serão gerados? '))
for jogo in range(qtd_jogos):
    print(f'Jogo {jogo}: ')
    for numeros in range(6):
        sorteados = list((randint(1, 60), randint(1, 60), randint(1, 60),
                          randint(1, 60), randint(1, 60), randint(1, 60)))
