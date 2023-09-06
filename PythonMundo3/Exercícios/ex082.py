#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas lsitas extras, que vão conter apenas os valores pares e os valores impares digitados, respectivamente
#Ao final, mostre o conteudo das três listas geradas

# Inicializa três listas vazias para armazenar os números digitados pelo usuário.
todos_numeros = []  # Todos os números digitados
numeros_pares = []  # Números pares digitados
numeros_impares = []  # Números ímpares digitados

# Inicia um loop infinito para permitir que o usuário insira números e decida se deseja continuar.
while True:
    # Solicita ao usuário que digite um número e o converte para inteiro, adicionando-o à lista todos_numeros.
    numero_digitado = int(input('Digite um número: '))
    todos_numeros.append(numero_digitado)

    # Solicita ao usuário que escolha se deseja continuar (S) ou sair (N), converte a resposta para maiúsculas e pega o primeiro caractere.
    escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]

    # Entra em um loop enquanto a escolha do usuário não for 'S' (Sim) ou 'N' (Não).
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()[0]

    # Se a escolha do usuário for 'N', sai do loop principal.
    if escolha == 'N':
        break

# Itera através da lista todos_numeros para separar os números pares e ímpares.
for numero in todos_numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)  # Adiciona números pares à lista numeros_pares.
    else:
        numeros_impares.append(numero)  # Adiciona números ímpares à lista numeros_impares.

# Exibe uma linha divisória.
print('-=' * 25)

# Exibe as três listas resultantes.
print(f'Todos os números digitados: {todos_numeros}')
print(f'Números pares digitados: {numeros_pares}')
print(f'Números ímpares digitados: {numeros_impares}')
