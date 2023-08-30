#Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

# Gera 5 números aleatórios entre 1 e 10
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

# Imprime o cabeçalho dos números sorteados
print('Os valores sorteados foram: ', end='')

# Loop para imprimir cada número com um espaço após ele
for n in numeros:
    print(f'{n} ', end='')

# Imprime uma nova linha para separar o próximo conteúdo
print()

# Imprime o maior valor sorteado
print(f'O maior valor sorteado foi {max(numeros)}')

# Imprime o menor valor sorteado
print(f'O menor valor sorteado foi {min(numeros)}')
