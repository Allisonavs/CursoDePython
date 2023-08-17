# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma Sequência de Fibonacci
# Fn = Fn - 1 + Fn - 2

# Menu do programa
print('-'*28)
print('Sequência de Fibonacci')
print('-'*28)

# Pergunta quantos termos deseja
n = int(input('Quantos termos você quer mostrar? '))

# Linha superior
print('~'*50)
# Crio as variáveis, pois para ter a sequência os termos iniciais sempre são 0 e 1
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')

# Crio a variável do contador
cont = 3

# Começo o laço
while cont <= n:
    t3 = t1 + t2                # Calcula o próximo termo somando os dois termos anteriores
    print(f' -> {t3}', end='')  # Imprime o próximo termo da sequência
    t1 = t2                     # Atualiza o primeiro termo para o valor do segundo termo
    t2 = t3                     # Atualiza o segundo termo para o valor do próximo termo
    cont += 1                   # Incrementa o contador de termos
print(' -> Fim')                # Imprime "Fim" quando o loop terminar
print('~'*50)
