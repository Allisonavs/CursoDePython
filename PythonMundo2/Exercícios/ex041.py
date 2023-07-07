# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master

from datetime import datetime

#O programa solicita o ano de nascimento do atleta

ano = int(input('Digite o ano de nascimento do atleta: '))

#O programa converte o ano para a idade do atleta

idade = datetime.now().year - ano

#O programa mostra a idade do atleta

print(f'O atleta tem {idade} anos')

#O programa indica em qual categoria o atleta se encontra:

if idade <= 9:
    print('O atleta é da categoria MIRIM')
elif idade <= 14:
    print('O atleta é da categoria INFANTIL')
elif idade <= 19:
    print('O atleta é da categoria JUNIOR')
elif idade <= 25:
    print('O atleta é da categoria SÊNIOR')
else:
    print('O atleta é da categoria MASTER')
