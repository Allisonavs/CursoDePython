import numpy as np  # Importa a biblioteca NumPy como 'np'.

# Crie uma matriz 3x3 preenchida com valores lidos pelo teclado
matriz = np.zeros((3, 3), dtype=int)  # Inicializa uma matriz 3x3 com zeros e tipo de dado inteiro.

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))  # Solicita um valor ao usuário.
        matriz[i, j] = valor  # Atribui o valor à posição correspondente na matriz.

# Mostre a matriz na tela
for linha in matriz:  # Itera pelas linhas da matriz.
    print(linha)  # Imprime cada linha da matriz.

