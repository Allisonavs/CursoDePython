#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas lsitas extras, que vão conter apenas os valores pares e os valores impares digitados, respectivamente
#Ao final, mostre o conteudo das três listas geradas

numt = []
nump = []
numi = []

while True:
    numt.append(int(input('Digite um número: ')))

    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if escolha == 'N':
        break

for numero in numt:
    if numero % 2 == 0:
        nump.append(numero)
    else:
        numi.append(numero)


print(f'Número digitados: {numt}')
print(f'Número pares digitados: {nump}')
print(f'Números impares digitados: {numi}')
