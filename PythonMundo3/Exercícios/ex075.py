#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9
#B) Em que posição foi digitado o primeiro valor 3
#C) Quais foram os números pares.

# Solicita que o usuário digite quatro números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite mais um: '))
n4 = int(input('O último agora: '))

# Cria uma tupla com os números digitados
tupla = (n1, n2, n3, n4)

# Imprime os números digitados na mesma linha
print(f'Você digitou os valores: ', end='')
for n in tupla:
    print(n, end=' ')

# Imprime a quantidade de vezes que o número 9 aparece na tupla
print(f'\nO número 9 apareceu {tupla.count(9)} vezes')

# Verifica se o número 3 está na tupla e imprime sua posição
if 3 in tupla:
    print(f'O primeiro 3 foi digitado na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')


# Imprime a quantidade de valores pares digitados
print(f'Os valores pares digitados foram:', end=' ')

# Verifica se o numero é par e mostra ele na tela
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
