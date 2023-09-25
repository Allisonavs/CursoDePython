# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esse resultados em um dicionário
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint

jogadas = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}

jogadas['jogador1'] = randint(1, 6)
jogadas['jogador2'] = randint(1, 6)
jogadas['jogador3'] = randint(1, 6)
jogadas['jogador4'] = randint(1, 6)

print(jogadas)