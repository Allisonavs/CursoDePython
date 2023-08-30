#Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import choice

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeros_aleatorios = ()
numero_menor = 11  # Inicializa a variável para um valor maior que qualquer número possível
numero_maior = 0  # Inicializa a variável para um valor menor que qualquer número possível

for c in range(5):
    numero_aleatorio = choice(numeros)  # Gera um número aleatório da tupla 'numeros'
    numeros_aleatorios += (numero_aleatorio,)  # Adiciona o número aleatório à tupla 'numeros_aleatorios'

    if numero_aleatorio < numero_menor:
        numero_menor = numero_aleatorio  # Atualiza 'numero_menor' se o número aleatório for menor
    elif numero_aleatorio > numero_maior:
        numero_maior = numero_aleatorio  # Atualiza 'numero_maior' se o número aleatório for maior

print(f'Os valores sorteados foram:',end=' ')
for n in numeros_aleatorios:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {numero_maior}')
print(f'O menor valor sorteado foi {numero_menor}')
