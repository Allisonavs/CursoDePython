#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente

num = []

while True:
    valor = int(input('Digite o valor: '))
    if valor not in num:
        print('Valor adicionado com sucesso...')
        num.append(valor)
    else:
        print('Valor já existente. Não adicionado!')

    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break

num.sort()
print(f'Você digitou os valores {num}')
