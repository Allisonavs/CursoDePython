# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for

#O programa pergunta de qual número o usuário deseja ver a tabuada

n1 = int(input('Escreva um número para ver a sua tábuada: '))

#Tela inicial do programa

print(f'Está é a tabuada do {n1}:')

#O laço é criado, de 1 a 10, fazendo os calculos para exibir a tabuada de n1
for c in range(1, 11):
    print(f'{n1} x {c:2} = {n1*c}')


#DESAFIO 009:

'''print(f'Está é a tabuada de {n1}:')
print('-' *13)
print(f'{n1} x  1 = {n1*1}')
print(f'{n1} x  2 = {n1*2}')
print(f'{n1} x  3 = {n1*3}')
print(f'{n1} x  4 = {n1*4}')
print(f'{n1} x  5 = {n1*5}')
print(f'{n1} x  6 = {n1*6}')
print(f'{n1} x  7 = {n1*7}')
print(f'{n1} x  8 = {n1*8}')
print(f'{n1} x  9 = {n1*9}')
print(f'{n1} x 10 = {n1*10}')
print('-' *13)'''
