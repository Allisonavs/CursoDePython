# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

# Bibliotecas
from random import randint
from time import sleep

# Lista de números
numeros = list()

# Função que sorteia 5 números e coloca-os dentro da lista
def sorteia():

    # Sorteia 5 números
    for i in range(5):
        numeros.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')

    for i, numero in enumerate(numeros):
        print(numero, end='')
        if i < len(numeros) -1:
            print(end=', ')
        sleep(0.5)

# Função que mostra a soma entre todos os valores pares sorteados
def somaPar():
    soma = 0

    # Soma os valores pares
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'\nSomando os valores pares de {numeros}, temos {soma}.')


# Programa Principal
sorteia()
somaPar()
