#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.

# Lista de times do Brasileirão Serie A 2023
times = (
    "Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Fluminense", "Bragantino",
    "Athletico-PR", "Fortaleza", "Atlético-MG", "Cuiabá", "São Paulo", "Cruzeiro",
    "Corinthians", "Internacional", "Goiás", "Bahia", "Santos", "Vasco da Gama",
    "Coritiba", "América-MG"
)


print('-='*20)
# Imprimir o título centralizado na tabela
print(f'{"Tabela Brasileirão Serie A 2023":^40}')

print('-='*20)

# Imprimir todos os times com suas posições
for pos, time in enumerate(times):
    print(f'{pos+1}º {time}')

print('-='*10)

# Imprimir os primeiros 5 colocados
print('Primeiros 5 colocados:\n')
for pos, time in enumerate(times[:5]):
    print(f'{pos+1}º {time}')

print('-='*10)

# Imprimir os últimos 4 colocados
print('Últimos 4 colocados:\n')
# Iniciar a contagem a partir do último elemento menos 3
for pos, time in enumerate(times[-4:], start=len(times)-3):
    print(f'{pos}º {time}')

print('-='*10)

# Imprimir os times em ordem alfabética
print('Times em ordem alfabética:\n')
for time in sorted(times):
    print(time)

print('-='*10)

# Encontrar e imprimir a posição do time "Cuiabá" na lista
print('Posição do CUIABÁ:\n')
print(f'{times.index("Cuiabá")+1}ª Posição')
