# Crie um programa onde o usuário possa digitar sete valores numéricaos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente

numeros = list()  # Inicializa uma lista vazia chamada 'numeros'.
numeros_pares = list()  # Inicializa uma lista vazia chamada 'numeros_pares' para armazenar números pares.
numeros_impares = list()  # Inicializa uma lista vazia chamada 'numeros_impares' para armazenar números ímpares.

for c in range(7):
    numero = int(input(f'Digite o {c + 1}º número: '))  # Solicita ao usuário um número inteiro.
    if numero % 2 == 0:
        numeros_pares.append(numero)  # Se o número for par, adiciona à lista 'numeros_pares'.
    elif numero % 2 == 1:
        numeros_impares.append(numero)  # Se o número for ímpar, adiciona à lista 'numeros_impares'.

numeros_pares.sort()  # Ordena a lista 'numeros_pares' em ordem crescente.
numeros_impares.sort()  # Ordena a lista 'numeros_impares' em ordem crescente.

numeros.append(numeros_pares)  # Adiciona a lista 'numeros_pares' à lista principal 'numeros'.
numeros.append(numeros_impares)  # Adiciona a lista 'numeros_impares' à lista principal 'numeros'.

print()

print(f'São pares os valores: {numeros[0]}')
print(f'São impares os valores: {numeros[1]}')

print()

print('São pares os números: ')
print(', '.join(map(str, numeros_pares)))  # Une os números pares com vírgulas e os exibe.

print('São ímpares os números: ')
print(', '.join(map(str, numeros_impares)))  # Une os números ímpares com vírgulas e os exibe.





