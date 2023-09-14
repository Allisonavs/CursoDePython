numeros = [[], []]  # Inicializa uma lista composta com duas sublistas: a primeira para pares e a segunda para ímpares.

for c in range(7):
    numero = int(input(f'Digite o {c + 1}º número: '))  # Solicita ao usuário um número inteiro.
    if numero % 2 == 0:
        numeros[0].append(numero)  # Se o número for par, adiciona à primeira sublista.
    else:
        numeros[1].append(numero)  # Se o número for ímpar, adiciona à segunda sublista.

numeros[0].sort()  # Ordena a primeira sublista em ordem crescente.
numeros[1].sort()  # Ordena a segunda sublista em ordem crescente.

print(f'São pares os valores: {", ".join(map(str, numeros[0]))}')
print(f'São ímpares os valores: {", ".join(map(str, numeros[1]))}')

