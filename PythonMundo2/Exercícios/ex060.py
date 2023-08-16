# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1=120

from time import sleep

# Pede para que o usuário digite um número para ver o fatorial dele
n = int(input('Digite um número: '))

# É criada a variável do fatorial
fatorial = 1

# Atribui o valor n para i, para poder usar no while e ainda indicá-la ao final do programa
i = n

#Mostra uma mensagem na tela
print(f'Calculando {n}!', end=' = ')
sleep(1)

# O laço é criado
while i >= 1:
    if i == 1:
        print(f'{i}', end=' = ')  # Coloca "=" no final da última iteração
    else:
        print(f'{i}', end=' x ')  # Coloca "x" no final da iteração
    fatorial *= i  # Multiplica a variável fatorial pelo valor atual de i
    i -= 1         # Decrementa o valor de i em 1 a cada iteração

# Mostra o resultado
print(f'{fatorial}')
