# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

matriz = [[], [] ,[]]

for c in range(3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    matriz[1].append(valor)
for c in range(3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(valor)

print(matriz[0])
print(matriz[1])
print(matriz[2])

print()

print(' '.join(map(str, matriz[0])))
print(' '.join(map(str, matriz[1])))
print(' '.join(map(str, matriz[2])))
