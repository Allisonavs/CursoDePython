# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se ja passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

#O programa pergunta se o usuário é do sexo feminino ou masculino

print('Você é do sexo Masculino ou Feminino?')
sexo = input('[M] - Masculino\n'
             '[F] - Feminino\n')
if sexo == 'F' or sexo == 'f':
    print('Você não possui alistamento obrigatório!')
    exit()

#O programa pede o ano de nascimento do usuário

ano = int(input('Informe seu ano de nascimento: '))

#O programa converte o ano de nascimento para idade

idade = datetime.now().year - ano

#O programa agora analisa se o usuário ainda vai se alistar, se está na hora de alistar ou se já passou do tempo
#e também calcula quanto tempo passou ou falta

if idade < 18:
    f = 18 - idade
    s = datetime.now().year + f
    if f == 1:
        print(f'Falta {f} ano para você se alistar')
    else:
        print(f'Faltam {f} anos para você se alistar')
    print(f'Seu alistamento será em {s}')
elif idade > 18:
    f = idade - 18
    s = datetime.now().year - f
    if f == 1:
        print(f'Se passou {f} ano do prazo de alistamento')
    else:
        print(f'Se passaram {f} anos do prazo de alistamento')
    print(f'Seu alistamento foi em {s}')
elif idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE')
