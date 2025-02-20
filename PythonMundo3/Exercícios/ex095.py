# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador

dados = dict()
jogadores = list()

while True:

    gols = list()

    # Solicita o nome do jogador
    dados['nome'] = str(input('Nome do jogador: '))

    # Solicita a quantidade de partidas jogadas pelo jogador
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    # Solicita a quantidade de gols feitos em cada partida
    for partida in range(dados['partidas']):
        gols.append(int(input(f'Quantos gols na partida {partida + 1}? ')))

    # Calcula o total de gols feitos durante o campeonato
    total_gols = sum(gols)

    # Adiciona a lista de gols e o total de gols ao dicionário
    dados['gols'] = gols
    dados['total_gols'] = total_gols

    # Adiciona os dados do jogador à lista de jogadores
    jogadores.append(dados.copy())
    dados.clear()

    # Pergunta se deseja continuar cadastrando jogadores
    if input('Quer continuar? [S/N] ').upper().strip()[0] == 'N':
        break

print()

# Exibe os dados de todos os jogadores cadastrados com formatação melhorada
print(f'{"Cod":<6} {"Nome":<20} {"Gols":<20} {"Total de Gols":<15}')
print('-' * 61)
for cod, jogador in enumerate(jogadores):
    print(f'{cod:<6} {jogador["nome"]:<20} {str(jogador["gols"]):<20} {jogador["total_gols"]:<15}')
print('-' * 61)

print()

while True:
    # Solicita o código do jogador para mostrar os detalhes
    jogador = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if jogador == 999:
        break
    if jogador >= len(jogadores):
        print('Jogador não cadastrado')
    else:
        # Exibe os detalhes do aproveitamento do jogador selecionado
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[jogador]["nome"]}:')
        for i, gol in enumerate(jogadores[jogador]['gols']):
            print(f'    No jogo {i+1} fez {gol} gols')
    print()

