# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1=120

#Pede para que o usuário digite um número para ver o fatorial dele
n = int(input('Digite um número: '))
fatorial = 1    # É criada a variavel do fatorial

#Atribui o valor n para i, para poder usar no while e ainda indiciar ela ao final do programa
i = n

#O laço é criado
while i >= 1:
    fatorial *= i   # Multiplica a variável fatorial pelo valor atual de i
    i -= 1   # Decrementa o valor de i em 1 a cada iteração

#Após o loop, a variável 'fatorial' conterá o fatorial do número digitado

#Mostra o resultado
print(f'O fatorial de {n}! é {fatorial}')
