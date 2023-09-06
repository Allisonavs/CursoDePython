#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente
#C) Se o valor 5 foi digitado e está ou não na lista

# Inicializa uma lista vazia para armazenar os números digitados pelo usuário.
num = []

# Inicia um loop infinito para permitir que o usuário insira números e decida se deseja continuar.
while True:
    # Solicita ao usuário que digite um número e o converte para inteiro, adicionando-o à lista.
    num.append(int(input('Digite um número: ')))

    # Solicita ao usuário que escolha se deseja continuar (S) ou sair (N), converte a resposta para maiúsculas e pega o primeiro caractere.
    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]

    # Entra em um loop enquanto a escolha do usuário não for 'S' (Sim) ou 'N' (Não).
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]

    # Se a escolha do usuário for 'N', sai do loop principal.
    if escolha == 'N':
        break

# Exibe a quantidade de números digitados pelo usuário.
print(f'Foram digitados {len(num)} números')

# Ordena a lista em ordem decrescente.
num.sort(reverse=True)

# Exibe a lista ordenada em ordem decrescente.
print(f'Lista em ordem decrescente: {num}')

# Verifica se o número 5 está na lista e exibe uma mensagem correspondente.
if 5 in num:
    print('Foi digitado o número 5, ele está na lista')
else:
    print('Não, o número 5 não foi digitado, ele não está na lista')
