# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

matriz_linha_um = list()
matriz_linha_dois = list()
matriz_linha_tres = list()
soma_pares = 0

for c in range(3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    matriz_linha_um.append(valor)
    if valor % 2 == 0:
        soma_pares += valor
for c in range(3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    matriz_linha_dois.append(valor)
    if valor % 2 == 0:
        soma_pares += valor
for c in range(3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    matriz_linha_tres.append(valor)
    if valor % 2 == 0:
        soma_pares += valor

soma_terceira_coluna = matriz_linha_um[2] + matriz_linha_dois[2] + matriz_linha_tres[2]
maior_valor_segunda_linha = max(matriz_linha_dois)

print(' '.join(map(str, matriz_linha_um)))
print(' '.join(map(str, matriz_linha_dois)))
print(' '.join(map(str, matriz_linha_tres)))

print(f'A soma de todos os valores pares digitados é igual a {soma_pares}')
print(f'A soma de todos os valores da terceira coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')
