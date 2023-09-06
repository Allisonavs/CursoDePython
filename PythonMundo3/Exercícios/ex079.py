#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente

# Cria uma lista vazia para armazenar os valores digitados pelo usuário
num = []

# Inicia um loop infinito para receber valores até que o usuário decida parar
while True:
    # Solicita ao usuário que digite um valor e converte para inteiro
    valor = int(input('Digite o valor: '))

    # Verifica se o valor já está na lista 'num'
    if valor not in num:
        print('Valor adicionado com sucesso...')
        # Adiciona o valor à lista 'num' se ele ainda não estiver presente
        num.append(valor)
    else:
        print('Valor já existente. Não adicionado!')

    # Pergunta ao usuário se deseja continuar e converte a resposta para maiúsculas
    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]

    # Garante que a resposta seja 'S' (Sim) ou 'N' (Não)
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]

    # Se o usuário escolher 'N', sai do loop
    if escolha == 'N':
        break

# Ordena a lista 'num' em ordem crescente
num.sort()

# Imprime os valores digitados pelo usuário
print(f'Você digitou os valores {num}')

