# Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.


# Função ficha com dois parâmetros opcionais 
def ficha(jog='<desconhecido>', gol=0):
    """
    -> Mostra a ficha de um jogador
    :param jog: Nome do jogador
    :param gol: Número de gols
    :return: Ficha do jogador
    """

    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Número de gols: '))

# Verifica se o número de gols é um número
if g.isnumeric():
    g = int(g)
else: # Se o número de gols não for um número ou não for informado nenhum número, g recebe 0
    g = 0

# Se o nome do jogador não for informado, n recebe uma string vazia
if n == '':
    ficha(gol=g)
else: # Se o nome do jogador for informado, chama a função ficha com os parâmetros informados
    ficha(n, g)
