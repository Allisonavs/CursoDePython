# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

matriz_linha_um = list()
matriz_linha_dois = list()
matriz_linha_tres = list()

for c in range(3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    matriz_linha_um.append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    matriz_linha_dois.append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    matriz_linha_tres.append(valor)

print(' '.join(map(str, matriz_linha_um)))
print(' '.join(map(str, matriz_linha_dois)))
print(' '.join(map(str, matriz_linha_tres)))
