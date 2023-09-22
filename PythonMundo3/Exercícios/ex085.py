# Crie um programa onde o usuário possa digitar sete valores numéricaos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente

numeros = [[], []]  # Inicializa uma lista composta com duas listas vazias, uma para números pares e outra para números ímpares.

for c in range(7):
    numero = int(input(f'Digite o {c + 1}º número: '))  # Solicita ao usuário um número inteiro.
    if numero % 2 == 0:
        numeros[0].append(numero)  # Se o número for par, adiciona à primeira lista de números pares.
    else:
        numeros[1].append(numero)  # Se o número for ímpar, adiciona à segunda lista de números ímpares.

numeros[0].sort()  # Ordena a lista de números pares em ordem crescente.
numeros[1].sort()  # Ordena a lista de números ímpares em ordem crescente.

print()

print(f'São pares os valores: {numeros[0]}')
print(f'São ímpares os valores: {numeros[1]}')

print()

print('São pares os números: ')
print(', '.join(map(str, numeros[0])))  # Une os números pares com vírgulas e os exibe.

print('São ímpares os números: ')
print(', '.join(map(str, numeros[1])))  # Une os números ímpares com vírgulas e os exibe.
