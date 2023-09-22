# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

# Cria uma matriz 3x3 preenchida com zeros.
matriz = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]

# Preenche a matriz com valores digitados pelo usuário.
for l in range(0, 3):  # Loop para as linhas (l) de 0 a 2.
    for c in range(0, 3):  # Loop para as colunas (c) de 0 a 2.
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

# Imprime a matriz formatada.
for l in range(0, 3):  # Loop para as linhas (l) de 0 a 2.
    for c in range(0, 3):  # Loop para as colunas (c) de 0 a 2.
        # Imprime o valor da matriz centralizado em 5 espaços.
        print(f'[{matriz[l][c]:^5}]', end='')
    # Imprime uma nova linha após imprimir uma linha completa da matriz.
    print()
