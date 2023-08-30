from colorama import Fore

times = ("Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Fluminense",
         "RB Bragantino", "Athlético-PR", "Fortaleza", "Atlético-MG",
         "Cuiabá", "São Paulo", "Cruzeiro", "Corinthians", "Internacional",
         "Goias", "Bahia", "Santos", "Vasco da Gama", "Coritiba", "América-MG")


def line():
    print('-' * 65)


line()
print(f'{"CAMPEONATO BRASILEIRO DE 2023":^65}')
line()
print(f'{"CLASSIFICAÇÃO | 21° Rodada":^65}')

for p, v in enumerate(times):

    if 0 <= p <= 3:
        print(Fore.BLUE + f'{str(p + 1):^2}° - {v}' + Fore.RESET)
    elif 4 <= p <= 5:
        print(Fore.GREEN + f'{str(p + 1):^2}° - {v}' + Fore.RESET)
    elif 6 <= p <= 11:
        print(Fore.MAGENTA + f'{str(p + 1):^2}° - {v}' + Fore.RESET)
    elif 12 <= p <= 15:
        print(f'{str(p + 1):^2}° - {v}')
    elif 16 <= p <= 19:
        print(Fore.RED + f'{str(p + 1):^2}° - {v}' + Fore.RESET)


line()

print(Fore.BLUE + f'{"Libertadores "}' + Fore.RESET +
      Fore.GREEN + f'{"Pré Libertadores "}' + Fore.RESET +
      Fore.MAGENTA + f'{"Sulamericana "}' + Fore.RESET +
      Fore.RED + f'{"Zona de Rebaixamento "}' + Fore.RESET)

print()

line()

print(f'{"5 PRIMEIROS COLOCADOS":^65}')

line()

for c in range(0, 5):
    print(f'{c + 1}° - {times[c]}')

line()

print(f'{"4 ÚLTIMOS COLOCADOS":^65}')

line()

for p, v in enumerate(times[-4:]):
    print(f'{times.index(v) + 1}° - {v}')

line()

print(f'{"TIMES EM ORDEM ALFABÉTICA":^65}')

line()

ordem_alfabetica = sorted(times)

for l in ordem_alfabetica:
    print(l)

line()

print(f'{"Posição do time do São Paulo":^65}')

line()

print(f'{times.index("São Paulo")}° - lugar')