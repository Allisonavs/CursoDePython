# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

# Cria uma matriz 3x3 preenchida com zeros.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variáveis para armazenar a soma dos valores pares e da terceira coluna, e o maior valor da segunda linha.
soma_pares = 0
soma_terceira_coluna = 0

# Preenche a matriz com valores digitados pelo usuário.
for l in range(0, 3):  # Loop para as linhas (l) de 0 a 2.
    for c in range(0, 3):  # Loop para as colunas (c) de 0 a 2.
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

        # Verifica se o valor é par e adiciona-o à soma dos valores pares.
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

        # Verifica se a coluna atual é a terceira (coluna 2) e adiciona o valor à soma da terceira coluna.
        if c == 2:
            soma_terceira_coluna += matriz[l][c]

# Imprime a matriz formatada.
for l in range(0, 3):  # Loop para as linhas (l) de 0 a 2.
    for c in range(0, 3):  # Loop para as colunas (c) de 0 a 2.
        # Imprime o valor da matriz centralizado em 5 espaços.
        print(f'[{matriz[l][c]:^5}]', end='')
    # Imprime uma nova linha após imprimir uma linha completa da matriz.
    print()

# Imprime as informações calculadas.
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
