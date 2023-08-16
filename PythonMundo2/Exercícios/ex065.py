# Crie um programa que leia vários números itneiros pelo teclado,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores

# Defino as variáveis que vou usar
total = 0  # Variável para armazenar a soma dos números digitados
cont = 0   # Variável para contar a quantidade de números digitados
cond = ''  # Variável para armazenar a condição de continuação do loop (S ou N)
menor = 0  # Variável para armazenar o menor número digitado
maior = 0  # Variável para armazenar o maior número digitado

# Crio o laço de repetição
while cond.lower() != 'n':
    n = int(input('\nDigite um número: '))
    total += n
    cont += 1
    media = total / cont

    if cont == 1:  # Se for o primeiro número digitado
        menor = n   # Define o primeiro número como o menor e o maior até o momento
        maior = n
    else:
        if n > maior:  # Se o número atual for maior que o maior número até o momento
            maior = n  # Atualiza o maior número
        elif n < menor:  # Se o número atual for menor que o menor número até o momento
            menor = n  # Atualiza o menor número

    cond = str(input('Deseja continuar? [S/N]: '))

# Exibe os resultados ao final do loop
print(f'\nA média é {media:.2f}')
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
