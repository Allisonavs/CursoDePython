# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esse resultados em um dicionário
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

# Importando funções necessárias
from random import randint  # Para gerar números aleatórios
from time import sleep  # Para introduzir atrasos na execução
from operator import itemgetter  # Para classificar o dicionário por valores

# Criando um dicionário para representar os jogadores e os resultados dos dados
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}

# Lista para armazenar o ranking dos jogadores
ranking = list()

# Exibindo os valores sorteados para cada jogador
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k.title()} tirou {v} no dado.')
    sleep(1)  # Atraso de 1 segundo para melhorar a visualização

# Classificando o dicionário de acordo com os valores dos dados em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Exibindo o ranking dos jogadores
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0].title()} com {v[1]}.')
