# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
# -1 para Binário
# -2 para Octal
# -3 para Hexadecimal

from time import sleep
from sys import exit

# Tela inicial do programa
print("-"*90)
print("Bem vindo ao conversos de base decimal, irei converter o número na base que desejar")
print("-"*90)

# O programa aguarda 1 segundo antes de permitir que o usuário digite o número

sleep(1.5)

# O programa lê um número que o usuário digita

numD = input('Digite um número inteiro: ')

# O programa analisa se o número digitado realmente é um número inteiro

if not numD.isdigit():
    print(f'{numD} não é um número inteiro')
    exit()

# Converte a entrada para um número inteiro, para que seja possivel em seguida realizar as operações com ele
numD = int(numD)

# Agora o programa lhe da opções de bases de conversão para o usuário e pede para ele escolher
print('Digite: \n'
      ' [1] - para binário\n'
      ' [2] - para octal\n'
      ' [3] - para hexadecimal')
e = input()

# O programa lê qual opção foi escolhida e fornece o número convertido (sem o prefixo de identificação)
if e == '1':
    print(f"{numD} em Binário: {numD:b}")
elif e == '2':
    print(f"{numD} em Octal: {numD:o}")
elif e == '3':
    print(f"{numD} em Hexadecimal: {numD:x}")
else:
    print(f'{e} não é uma opção válida, tente novamente!')
