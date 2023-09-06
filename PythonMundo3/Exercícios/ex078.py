#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

# Cria uma lista vazia para armazenar os números digitados
num = []

# Inicializa as variáveis para armazenar o maior e o menor número digitado
mai = 0
men = 0

# Loop para pedir ao usuário que digite 5 números
for c in range(5):
    # Solicita ao usuário que digite um número para a posição atual do loop
    num.append(int(input(f'Digite um número para a Posição {c}: ')))

    # Verifica se este é o primeiro número digitado
    if c == 0:
        # Se for o primeiro número, atribui a ele tanto o maior quanto o menor valor
        mai = men = num[c]
    else:
        # Se não for o primeiro número, compara com os valores atuais de maior e menor
        if num[c] > mai:
            mai = num[c]
        elif num[c] < men:
            men = num[c]

# Exibe a lista de números digitados pelo usuário
print(f'Você digitou os valores {num}')

# Exibe o maior número e suas posições na lista
print(f'O maior número digitado foi: {mai} nas posições ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}... ', end='')

# Exibe o menor número e suas posições na lista
print(f'\nO menor número digitado foi: {men} nas posições ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}... ', end='')
