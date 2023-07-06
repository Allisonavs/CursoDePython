# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se ja passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

#O programa pede o ano de nascimento do usuário:

ano = int(input('Informe seu ano de nascimento: '))

#O programa converte o ano de nascimento para idade

idade = datetime.now().year - ano

#O programa agora analisa se o usuário ainda vai se alistar, se está na hora de alistar ou se já passou do tempo
#e também calcula quanto tempo passou ou falta

if idade < 18:
    f = 18 - idade
    if f == 1:
        print(f'Falta {f} ano para você se alistar')
    else:
        print(f'Faltam {f} anos para você se alistar')
elif idade > 18:
    f = idade - 18
    if f == 1:
        print(f'Se passou {f} ano do prazo de alistamento')
    else:
        print(f'Se passaram {f} anos do prazo de alistamento')
elif idade == 18:
    print('Você está dentro do prazo de alistamento')
