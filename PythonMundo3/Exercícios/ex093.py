# Crie um programa que gerencie o aproveitamento de um jogador de futubol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de feitos durante o campeonato

# Inicialização do dicionário e da lista a serem usados
aproveitamento = dict()
gols = list()

# Solicita ao usuário o nome do jogador e a quantidade de partidas jogadas
aproveitamento['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))

# Pergunta quantos gols o jogador fez em cada partida e armazena na lista 'gols'
for partida in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))

# Adiciona a lista 'gols' no dicionário 'aproveitamento', usando a chave 'gols'
aproveitamento['gols'] = gols[:]

# Calcula o total de gols e adiciona ao dicionário 'aproveitamento'
aproveitamento['total'] = sum(gols)

# Mostra o conteúdo do dicionário
print('-='*30)
print(aproveitamento)
print('-='*30)

# Com um laço, mostra o valor de cada item do dicionário
for chave, valor in aproveitamento.items():
    print(f'O campo {chave} tem o valor {valor}.')

print('-='*30)

# Mostra o número de partidas jogadas pelo jogador
print(f'O jogador {aproveitamento["nome"]} jogou {partidas} partidas.')

# Mostra quantos gols ele fez em cada partida
for partida in range(partidas):
    print(f'     => Na partida {partida+1}, fez {aproveitamento["gols"][partida]} gols.')

# Mostra o total de gols no campeonato
print(f'Foi um total de {aproveitamento["total"]} gols.')
